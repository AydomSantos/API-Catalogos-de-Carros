# 🚗 API de Catálogo de Veículos

API REST para gerenciamento de catálogo de veículos, desenvolvida com Flask. O projeto suporta tanto SQLite quanto MongoDB como banco de dados.

## 📋 Índice
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Uso](#-uso)
- [Endpoints](#-endpoints)
- [Adaptação para MongoDB](#-adaptação-para-mongodb)
- [Testes](#-testes)

## 🚀 Tecnologias

- Python 3.x
- Flask
- SQLAlchemy (para SQLite)
- Flask-JWT-Extended
- MongoDB (opcional)

## 📁 Estrutura do Projeto

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd [NOME_DO_DIRETORIO]
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

1. Crie um arquivo `.env`:
```env
FLASK_APP=run.py
FLASK_ENV=development
JWT_SECRET_KEY=sua-chave-secreta-aqui
```

2. Inicialize o banco de dados:
```bash
python -m scripts.init_db
```

3. (Opcional) Popule o banco com dados de teste:
```bash
python -m scripts.seed_vehicles
```

## 🏃‍♂️ Uso

1. Execute a aplicação:
```bash
python run.py
```

2. Acesse a API em `http://localhost:5000`

## 🛣️ Endpoints

### Autenticação
- `POST /login`
  ```json
  {
    "username": "admin",
    "password": "senha_segura"
  }
  ```

### Veículos
- `GET /vehicles` - Lista todos os veículos
- `GET /vehicles/<id>` - Obtém um veículo específico
- `POST /admin/vehicles` - Cria novo veículo (requer auth)
- `PUT /admin/vehicles/<id>` - Atualiza veículo (requer auth)
- `DELETE /admin/vehicles/<id>` - Remove veículo (requer auth)

### Exemplo de Veículo
```json
{
    "nome": "Corolla Cross",
    "marca": "Toyota",
    "modelo": "XRX Hybrid",
    "foto": "url_da_foto",
    "valor": 184990.00
}
```

## 🔄 Adaptação para MongoDB

Para usar MongoDB ao invés de SQLite, siga estas etapas:

1. Atualize o `requirements.txt`:
```text
flask
flask-pymongo
flask-jwt-extended
python-dotenv
```

2. Modifique `app/extensions.py`:
```python
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

mongo = PyMongo()
jwt = JWTManager()
```

3. Atualize `app/config/config.py`:
```python
class Config:
    MONGO_URI = 'mongodb://localhost:27017/vehicles_db'
    JWT_SECRET_KEY = 'sua-chave-secreta'
```

4. Modifique o modelo `app/models/vehicle.py`:
```python
from datetime import datetime

class Vehicle:
    @staticmethod
    def create(data):
        return {
            'nome': data['nome'],
            'marca': data['marca'],
            'modelo': data['modelo'],
            'foto': data.get('foto', ''),
            'valor': float(data['valor']),
            'created_at': datetime.utcnow()
        }
```

5. Atualize as rotas em `app/routes/vehicles.py`:
```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import mongo
from bson import ObjectId

vehicles_bp = Blueprint('vehicles', __name__)

@vehicles_bp.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = list(mongo.db.vehicles.find().sort('valor', 1))
    for v in vehicles:
        v['_id'] = str(v['_id'])
    return jsonify(vehicles)

@vehicles_bp.route('/admin/vehicles', methods=['POST'])
@jwt_required()
def create_vehicle():
    data = request.get_json()
    result = mongo.db.vehicles.insert_one(Vehicle.create(data))
    return jsonify({'id': str(result.inserted_id)}), 201
```

6. Crie um script de inicialização para MongoDB:
```python
from app import create_app
from app.extensions import mongo
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Criar índices
    mongo.db.vehicles.create_index('valor')
    
    # Criar usuário admin
    if not mongo.db.users.find_one({'username': 'admin'}):
        mongo.db.users.insert_one({
            'username': 'admin',
            'password': generate_password_hash('senha_segura'),
            'role': 'admin'
        })
```

## 🧪 Testes

Para testar a API, você pode usar o Postman ou cURL:

1. Login (obter token):
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"senha_segura"}'
```

2. Criar veículo:
```bash
curl -X POST http://localhost:5000/admin/vehicles \
  -H "Authorization: Bearer SEU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Civic",
    "marca": "Honda",
    "modelo": "EXL",
    "foto": "url_da_foto",
    "valor": 150000.00
  }'
```

## 📝 Principais Diferenças entre SQLite e MongoDB

### SQLite
- Banco de dados relacional
- Esquema definido (models com colunas)
- Transações ACID
- Ideal para aplicações menores
- Arquivo único local

### MongoDB
- Banco de dados NoSQL
- Esquema flexível
- Documentos JSON
- Melhor para escala horizontal
- Requer servidor separado

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.