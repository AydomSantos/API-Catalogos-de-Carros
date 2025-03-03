from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models.vehicle import Vehicle

vehicles_bp = Blueprint('vehicles', __name__)

@vehicles_bp.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.order_by(Vehicle.valor).all()
    return jsonify([{
        'id': v.id,
        'nome': v.nome,
        'marca': v.marca,
        'modelo': v.modelo,
        'foto': v.foto,
        'valor': v.valor,
        'created_at': v.created_at
    } for v in vehicles]), 200

@vehicles_bp.route('/vehicles/<int:id>', methods=['GET'])
def get_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    return jsonify({
        'id': vehicle.id,
        'nome': vehicle.nome,
        'marca': vehicle.marca,
        'modelo': vehicle.modelo,
        'foto': vehicle.foto,
        'valor': vehicle.valor,
        'created_at': vehicle.created_at
    }), 200

@vehicles_bp.route('/admin/vehicles', methods=['POST'])
@jwt_required()
def create_vehicle():
    data = request.get_json()
    vehicle = Vehicle.create(data)
    db.session.add(vehicle)
    db.session.commit()
    return jsonify({
        'id': vehicle.id,
        'nome': vehicle.nome,
        'marca': vehicle.marca,
        'modelo': vehicle.modelo,
        'foto': vehicle.foto,
        'valor': vehicle.valor
    }), 201

@vehicles_bp.route('/admin/vehicles/<int:id>', methods=['PUT'])
@jwt_required()
def update_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    data = request.get_json()
    
    for key, value in data.items():
        setattr(vehicle, key, value)
    
    db.session.commit()
    return jsonify({'message': 'Veículo atualizado com sucesso'}), 200

@vehicles_bp.route('/admin/vehicles/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({'message': 'Veículo deletado com sucesso'}), 200






