from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required
from app.extensions import mongo
from bson import ObjectId
from datetime import datetime


vehicles_bp = Blueprint('vehicles', __name__)

@vehicles_bp.route('/vehicles', methods=['GET'])
def get_vehicles():
    try:
        # Check MongoDB connection
        try:
            mongo.cx.server_info()
            vehicles = list(mongo.db.vehicles.find())
            for vehicle in vehicles:
                vehicle['_id'] = str(vehicle['_id'])
            return jsonify(vehicles), 200  # Fixed: return vehicles list instead of vehicle
            
        except Exception as e:
            current_app.logger.error(f"Database connection error: {str(e)}")
            return jsonify({'error': 'Database connection not established'}), 500

    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return jsonify({'error': 'Error accessing database'}), 500
        
@vehicles_bp.route('/vehicles/<int:id>', methods=['GET'])
def get_vehicle(id):
    vehicle = mongo.db.vehicles.find_one({'_id': ObjectId(id)})
    return jsonify({
        'id': str(vehicle['_id']),
        'nome': vehicle['nome'],
        'marca': vehicle['marca'],
        'modelo': vehicle['modelo'],
        'foto': vehicle['foto'],
        'valor': vehicle['valor'],
        'created_at': vehicle['created_at']
    }), 200

@vehicles_bp.route('/admin/vehicles', methods=['POST'])
@jwt_required()
def create_vehicle():
    try:
        # Check MongoDB connection properly
        try:
            mongo.cx.server_info()
        except Exception as e:
            current_app.logger.error(f"Database connection error: {str(e)}")
            return jsonify({'error': 'Database connection not established'}), 500

        # Validate request data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Validate required fields
        required_fields = ['nome', 'marca', 'modelo', 'valor']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400

        # Add creation timestamp
        data['created_at'] = datetime.now()

        # Insert vehicle with proper error handling
        try:
            result = mongo.db.vehicles.insert_one(data)
            vehicle = mongo.db.vehicles.find_one({'_id': result.inserted_id})
            if vehicle is None:
                raise Exception("Vehicle not found after creation")
            
            return jsonify({
                'id': str(vehicle['_id']),
                'nome': vehicle['nome'],
                'marca': vehicle['marca'],
                'modelo': vehicle['modelo'],
                'foto': vehicle.get('foto', ''),
                'valor': vehicle['valor']
            }), 201
            
        except Exception as e:
            current_app.logger.error(f"Database error: {str(e)}")
            return jsonify({'error': 'Error creating vehicle'}), 500
            
    except Exception as e:
        current_app.logger.error(f"Request error: {str(e)}")
        return jsonify({'error': 'Invalid request'}), 400
@vehicles_bp.route('/admin/vehicles/<int:id>', methods=['PUT'])
@jwt_required()
def update_vehicle(id):
    data = request.get_json()
    result = mongo.db.vehicles.update_one(
        {'_id': ObjectId(id)}, 
        {'$set': data}
    )
    if result.modified_count == 0:
        return jsonify({'message': 'Veículo não encontrado'}), 404
    return jsonify({'message': 'Veículo atualizado com sucesso'}), 200

@vehicles_bp.route('/admin/vehicles/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_vehicle(id):
    result = mongo.db.vehicles.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({'message': 'Veículo não encontrado'}), 404
    return jsonify({'message': 'Veículo deletado com sucesso'}), 200






