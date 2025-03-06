from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.extensions import mongo
from app.routes.auth import auth_bp
from app.routes.vehicles import vehicles_bp
import os
from dotenv import load_dotenv
from datetime import timedelta
from pymongo.errors import ConfigurationError, PyMongoError

def create_app():
    app = Flask(__name__)
    
    # Configurar CORS
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Load environment variables
    load_dotenv()
    
    # Configure MongoDB with error handling
    mongo_uri = os.getenv('MONGO_URI')
    if not mongo_uri:
        app.logger.error("MONGO_URI not found in environment variables")
        raise ValueError("MONGO_URI configuration is missing")
    
    # Ensure database name is included in URI
    if not 'vehicles_db' in mongo_uri:
        mongo_uri += 'vehicles_db'
    
    app.config['MONGO_URI'] = mongo_uri
    
    # Configure JWT
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
    app.config['JWT_ERROR_MESSAGE_KEY'] = 'msg'
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'
    
    try:
        # Initialize extensions
        mongo.init_app(app)
        jwt = JWTManager(app)
        
        # Test MongoDB connection
        with app.app_context():
            mongo.db.command('ping')
            app.logger.info("MongoDB connection successful")
            
    except PyMongoError as e:  # Changed exception type
        app.logger.error(f"MongoDB error: {str(e)}")
        raise
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(vehicles_bp)
    
    @app.route('/')
    def index():
        return {
            'message': 'API de Catálogo de Veículos',
            'status': 'online',
            'version': '1.0',
            'endpoints': {
                'auth': '/login',
                'vehicles': '/vehicles'
            }
        }
    
    return app



