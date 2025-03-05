🚗 API de Catálogo de Veículos

API REST para gerenciamento de catálogo de veículos, desenvolvida com Flask e MongoDB Atlas.

📋 Índice

Tecnologias

Estrutura do Projeto

Instalação

Configuração

Uso

Endpoints

Testes

Solução de Problemas

Licença

🚀 Tecnologias

Python 3.x

Flask

Flask-PyMongo

Flask-JWT-Extended

MongoDB Atlas

Python-dotenv

📁 Estrutura do Projeto

api-catalogos-de-carros/
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   └── routes/
│       ├── auth.py
│       └── vehicles.py
├── .env
├── .gitignore
├── requirements.txt
└── run.py

🔧 Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/api-catalogos-de-carros.git
cd api-catalogos-de-carros

Crie e ative o ambiente virtual:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

⚙️ Configuração

Crie um arquivo .env na raiz do projeto e adicione:

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

Para iniciar o servidor, execute:

python run.py

A API estará disponível em: http://localhost:5000

🛣️ Endpoints

🔑 Autenticação

POST /login - Gera token JWT

{
  "username": "admin",
  "password": "sua_senha"
}

🚗 Veículos

Método

Endpoint

Descrição

Autenticação

GET

/vehicles

Lista todos os veículos

Não

GET

/vehicles/

Obtém um veículo específico

Não

POST

/admin/vehicles

Cria novo veículo

Sim

PUT

/admin/vehicles/

Atualiza veículo

Sim

DELETE

/admin/vehicles/

Remove veículo

Sim

Exemplo de corpo para POST/PUT:

{
    "nome": "Civic",
    "marca": "Honda",
    "modelo": "EXL",
    "foto": "http://exemplo.com/foto.jpg",
    "valor": 150000.00
}

🧪 Testes

🔑 Login (Obter Token)

Método: POST

URL: http://localhost:5000/login

Headers: Content-Type: application/json

Body:

{
    "username": "admin",
    "password": "sua_senha"
}

🚗 Criar Veículo

Método: POST

URL: http://localhost:5000/admin/vehicles

Headers:

Content-Type: application/json
Authorization: Bearer <seu_token_jwt>

Body:

{
    "nome": "Civic",
    "marca": "Honda",
    "modelo": "EXL",
    "foto": "http://exemplo.com/foto.jpg",
    "valor": 150000.00
}

🔧 Solução de Problemas

🔴 Erros Comuns

Erro 500 - Conexão com MongoDB

Verifique a URI no .env

Confirme acesso pelo IP no MongoDB Atlas

Teste a conexão usando ferramentas como MongoDB Compass

Erro 401/403 - Autenticação

Verifique o prefixo Bearer no header Authorization

Confira a validade do token JWT

Valide a chave secreta JWT no .env

Erro 400 - Requisição Inválida

Verifique o formato JSON do corpo da requisição

Confira se todos os campos obrigatórios estão presentes: nome, marca, modelo, valor

📜 Licença

Este projeto está sob a licença MIT. Para mais detalhes, consulte o arquivo LICENSE.
