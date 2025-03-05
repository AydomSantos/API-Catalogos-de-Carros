# 🚗 API de Catálogo de Veículos

API REST para gerenciamento de catálogo de veículos, desenvolvida com Flask e MongoDB Atlas.

## 📋 Índice
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Uso](#-uso)
- [Endpoints](#-endpoints)
- [Testes](#-testes)
- [Solução de Problemas](#-solução-de-problemas)
- [Licença](#-licença)

## 🚀 Tecnologias
- Python 3.x
- Flask
- Flask-PyMongo
- Flask-JWT-Extended
- MongoDB Atlas
- Python-dotenv

## 📁 Estrutura do Projeto
api-catalogos-de-carros/
├── app/
│ ├── init.py
│ ├── extensions.py
│ └── routes/
│ ├── auth.py
│ └── vehicles.py
├── .env
├── .gitignore
├── requirements.txt
└── run.py

Copy

## 🔧 Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/api-catalogos-de-carros.git
cd api-catalogos-de-carros
Crie e ative o ambiente virtual:

bash
Copy
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
Instale as dependências:

bash
Copy
pip install -r requirements.txt
⚙️ Configuração
Crie um arquivo .env na raiz do projeto com:

env
Copy
MONGO_URI=sua_uri_mongodb_atlas
JWT_SECRET_KEY=sua_chave_secreta_jwt
Configuração do MongoDB Atlas:

Crie uma conta no MongoDB Atlas

Configure um novo cluster

Adicione seu IP à lista de permissões

Crie um usuário com permissões de leitura/escrita

Obtenha a URI de conexão no formato:
mongodb+srv://<usuario>:<senha>@cluster.mongodb.net/<database>

🏃‍♂️ Uso
Inicie o servidor:

bash
Copy
python run.py
A API estará disponível em: http://localhost:5000

🛣️ Endpoints
Autenticação
POST /login - Gera token JWT

json
Copy
{
  "username": "admin",
  "password": "sua_senha"
}
Veículos
Método	Endpoint	Descrição	Autenticação
GET	/vehicles	Lista todos os veículos	Não
GET	/vehicles/<id>	Obtém um veículo específico	Não
POST	/admin/vehicles	Cria novo veículo	Sim
PUT	/admin/vehicles/<id>	Atualiza veículo	Sim
DELETE	/admin/vehicles/<id>	Remove veículo	Sim
Exemplo de corpo (POST/PUT):

json
Copy
{
    "nome": "Civic",
    "marca": "Honda",
    "modelo": "EXL",
    "foto": "http://exemplo.com/foto.jpg",
    "valor": 150000.00
}
🧪 Testes
Login (Obter Token)
Requisição:

Método: POST

URL: http://localhost:5000/login

Headers: Content-Type: application/json

Body:

json
Copy
{
    "username": "admin",
    "password": "sua_senha"
}
Criar Veículo
Requisição:

Método: POST

URL: http://localhost:5000/admin/vehicles

Headers:

Copy
Content-Type: application/json
Authorization: Bearer <seu_token_jwt>
Body:

json
Copy
{
    "nome": "Civic",
    "marca": "Honda",
    "modelo": "EXL",
    "foto": "http://exemplo.com/foto.jpg",
    "valor": 150000.00
}
🔧 Solução de Problemas
Erros Comuns
Erro 500 - Conexão com MongoDB

Verifique a URI no .env

Confirme acesso pelo IP no MongoDB Atlas

Teste a conexão usando ferramentas como MongoDB Compass

Erro 401/403 - Autenticação

Verifique o prefixo Bearer no header Authorization

Confira a validade do token JWT

Valide a chave secreta JWT no .env

Erro 400 - Requisição Inválida

Verifique o formato JSON do corpo

Confira campos obrigatórios:

nome, marca, modelo, valor
