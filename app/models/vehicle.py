from app.extensions import db
from datetime import datetime

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    foto = db.Column(db.String(200))
    valor = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def create(data):
        return Vehicle(
            nome=data['nome'],
            marca=data['marca'],
            modelo=data['modelo'],
            foto=data.get('foto', ''),
            valor=float(data['valor'])
        )
