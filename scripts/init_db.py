import sys
import os

# Adiciona o diretório raiz do projeto ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()

with app.app_context():
    # Recria o banco de dados
    db.drop_all()
    db.create_all()
    
    # Cria usuário admin
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', role='admin')
        admin.set_password('senha_segura')
        db.session.add(admin)
        db.session.commit()
        print("Usuário admin criado com sucesso!") 