from flask import Flask
from .config.config import Config
from .extensions import db, jwt
from .routes.vehicles import vehicles_bp
from .routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializa extensões
    db.init_app(app)
    jwt.init_app(app)
    
    # Registra blueprints
    app.register_blueprint(vehicles_bp)
    app.register_blueprint(auth_bp)
    
    # Cria as tabelas do banco de dados
    with app.app_context():
        db.create_all()
    
    return app



