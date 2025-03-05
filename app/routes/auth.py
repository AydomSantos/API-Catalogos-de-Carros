from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token
from app.extensions import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        # Check MongoDB connection and database status
        try:
            # Better way to check MongoDB connection
            mongo.cx.server_info()
        except Exception as e:
            current_app.logger.error(f"Database connection failed: {str(e)}")
            return jsonify({"msg": "Database connection error"}), 500

        data = request.get_json()
        
        # Validate input
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"msg": "Missing username or password"}), 400
            
        # Find user with error handling
        try:
            user = mongo.db.users.find_one({'username': data['username']})
            if user is None:
                return jsonify({"msg": "User not found"}), 401
        except Exception as e:
            current_app.logger.error(f"Database query error: {str(e)}")
            return jsonify({"msg": "Database error"}), 500
        if not user:
            return jsonify({"msg": "User not found"}), 401
            
        # Check password
        if check_password_hash(user['password'], data['password']):
            access_token = create_access_token(
                identity=str(user['_id']),
                expires_delta=timedelta(days=1)
            )
            return jsonify({"access_token": access_token}), 200
            
        return jsonify({"msg": "Invalid credentials"}), 401
        
    except Exception as e:
        current_app.logger.error(f"Login error: {str(e)}")
        return jsonify({"msg": "Internal server error"}), 500

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"msg": "Missing username or password"}), 400
            
        # Check if user exists
        if mongo.db.users.find_one({'username': data['username']}):
            return jsonify({"msg": "Username already exists"}), 400
            
        # Create user
        user = {
            'username': data['username'],
            'password': generate_password_hash(data['password']),
            'role': 'admin',
            'created_at': datetime.now()
        }
        
        result = mongo.db.users.insert_one(user)
        
        return jsonify({
            'msg': 'User created successfully',
            'id': str(result.inserted_id)
        }), 201
        
    except Exception as e:
        current_app.logger.error(f"Registration error: {str(e)}")
        return jsonify({"msg": "Internal server error"}), 500