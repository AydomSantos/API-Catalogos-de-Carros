
Apply
# 🚗 API de Catálogo de VeículosAPI REST para gerenciamento de catálogo de veículos, desenvolvida com Flask e MongoDB Atlas.## 📋 Índice- [Tecnologias](#-tecnologias)- [Estrutura do Projeto](#-estrutura-do-projeto)- [Instalação](#-instalação)- [Configuração](#-configuração)- [Uso](#-uso)- [Endpoints](#-endpoints)- [Testes](#-testes)- [Solução de Problemas](#-solução-de-problemas)## 🚀 Tecnologias- Python 3.x- Flask- Flask-PyMongo- Flask-JWT-Extended- MongoDB Atlas- Python-dotenv## 📁 Estrutura do Projeto
api-catalogos-de-carros/ ├── app/ │ ├── init.py │ ├── extensions.py │ ├── routes/ │ │ ├── auth.py │ │ └── vehicles.py ├── .env ├── .gitignore ├── requirements.txt └── run.py

plaintext

## 🔧 Instalação1. Clone o repositório:```bashgit clone https://github.com/seu-usuario/api-catalogos-de-carros.gitcd api-catalogos-de-carros
Crie e ative o ambiente virtual:
bash
Run
python -m venv venvvenv\Scripts\activate
Instale as dependências:
bash
Run
pip install -r requirements.txt
⚙️ Configuração
Crie um arquivo .env:
env

MONGO_URI=sua_uri_do_mongodb_atlasJWT_SECRET_KEY=sua_chave_jwt_secreta
Configure o MongoDB Atlas:
Crie uma conta no MongoDB Atlas
Configure um novo cluster
Obtenha a URI de conexão
Adicione a URI no arquivo .env
🏃‍♂️ Uso
Execute a aplicação:
bash
Run
python run.py
Acesse a API em http://localhost:5000
🛣️ Endpoints
Autenticação
POST /login - Login do usuário
json

{  "username": "admin",  "password": "sua_senha"}
Veículos
GET /vehicles - Lista todos os veículos
GET /vehicles/<id> - Obtém um veículo específico
POST /admin/vehicles - Cria novo veículo (requer auth)
PUT /admin/vehicles/<id> - Atualiza veículo (requer auth)
DELETE /admin/vehicles/<id> - Remove veículo (requer auth)
Exemplo de Veículo
json

{    "nome": "Civic",    "marca": "Honda",    "modelo": "EXL",    "foto": "url_da_foto",    "valor": 150000.00}
🧪 Testes
Usando Insomnia:
Login (obter token):
Método: POST
URL: http://localhost:5000/login
Headers: Content-Type: application/json
Body:
json

{    "username": "admin",    "password": "sua_senha"}
Criar veículo:
Método: POST
URL: http://localhost:5000/admin/vehicles
Headers:
Content-Type: application/json
Authorization: Bearer seu_token_jwt
Body:
json

{    "nome": "Civic",    "marca": "Honda",    "modelo": "EXL",    "foto": "url_da_foto",    "valor": 150000.00}
🔧 Solução de Problemas
Erros Comuns:
Erro de Conexão MongoDB:
Verifique a URI do MongoDB no arquivo .env
Confirme se o IP está liberado no MongoDB Atlas
Verifique as credenciais de acesso
Erro de Autenticação (401/422):
Certifique-se de incluir o token JWT
Use o prefixo "Bearer" no token
Verifique se o token não está expirado
Erro ao Criar Veículo:
Verifique se todos os campos obrigatórios estão presentes
Confirme o formato correto do JSON
Verifique a conexão com o banco de dados
📄 Licença
Este projeto está sob a licença MIT.

plaintext

The key updates include:- Removed SQLite references- Added MongoDB Atlas specific configuration- Updated installation and setup instructions- Added troubleshooting section- Updated project structure- Added detailed testing instructions for InsomniaWould you like me to explain any specific section in more detail?
AydomSantos
Copy
Delete
faça o readm com essas informações 
Trae AI
Used 1 Reference
README.md
I'll create a new README with the current project information:

README.md
Apply
# 🚗 API de Catálogo de VeículosAPI REST para gerenciamento de catálogo de veículos, desenvolvida com Flask e MongoDB Atlas.## 📋 Índice- [Tecnologias](#-tecnologias)- [Estrutura do Projeto](#-estrutura-do-projeto)- [Instalação](#-instalação)- [Configuração](#-configuração)- [Uso](#-uso)- [Endpoints](#-endpoints)- [Testes](#-testes)- [Solução de Problemas](#-solução-de-problemas)## 🚀 Tecnologias- Python 3.x- Flask- Flask-PyMongo- Flask-JWT-Extended- MongoDB Atlas- Python-dotenv## 📁 Estrutura do Projeto
api-catalogos-de-carros/ ├── app/ │ ├── init.py │ ├── extensions.py │ ├── routes/ │ │ ├── auth.py │ │ └── vehicles.py ├── .env ├── .gitignore ├── requirements.txt └── run.py

plaintext

## 🔧 Instalação1. Clone o repositório:```bashgit clone https://github.com/seu-usuario/api-catalogos-de-carros.gitcd api-catalogos-de-carros
Crie e ative o ambiente virtual:
bash
Run
python -m venv venvvenv\Scripts\activate
Instale as dependências:
bash
Run
pip install -r requirements.txt
⚙️ Configuração
Configure o arquivo .env:
env

MONGO_URI=mongodb+srv://seu_usuario:sua_senha@seu_cluster.mongodb.net/JWT_SECRET_KEY=sua_chave_jwt_secreta
Configure o MongoDB Atlas:
Crie uma conta no MongoDB Atlas
Configure um novo cluster
Obtenha a URI de conexão
Adicione a URI no arquivo .env
🏃‍♂️ Uso
Execute a aplicação:
bash
Run
python run.py
Acesse a API em http://localhost:5000
🛣️ Endpoints
Autenticação
POST /login - Login do usuário
json

{  "username": "admin",  "password": "sua_senha"}
Veículos
GET /vehicles - Lista todos os veículos
GET /vehicles/<id> - Obtém um veículo específico
POST /admin/vehicles - Cria novo veículo (requer auth)
PUT /admin/vehicles/<id> - Atualiza veículo (requer auth)
DELETE /admin/vehicles/<id> - Remove veículo (requer auth)
Exemplo de Veículo
json

{    "nome": "Civic",    "marca": "Honda",    "modelo": "EXL",    "foto": "url_da_foto",    "valor": 150000.00}
🧪 Testes com Insomnia
Login (obter token):
Método: POST
URL: http://localhost:5000/login
Headers: Content-Type: application/json
Body:
json

{    "username": "admin",    "password": "sua_senha"}
Criar veículo:
Método: POST
URL: http://localhost:5000/admin/vehicles
Headers:
Content-Type: application/json
Authorization: Bearer seu_token_jwt
Body:
json

{    "nome": "Civic",    "marca": "Honda",    "modelo": "EXL",    "foto": "url_da_foto",    "valor": 150000.00}
🔧 Solução de Problemas
Erros Comuns:
Erro de Conexão MongoDB (500):
Verifique a URI do MongoDB no arquivo .env
Confirme se o IP está liberado no MongoDB Atlas
Verifique as credenciais de acesso
Erro de Autenticação (401/422):
Certifique-se de incluir o token JWT
Use o prefixo "Bearer" no token
Verifique se o token não está expirado
Erro ao Criar Veículo (400):
Verifique se todos os campos obrigatórios estão presentes
Confirme o formato correto do JSON
Verifique a conexão com o banco de dados
📄 Licença
Este projeto está sob a licença MIT.

plaintext

The key updates include:- Removed SQLite references- Updated technology stack- Added MongoDB Atlas configuration- Simplified installation steps- Added detailed testing instructions for Insomnia- Added troubleshooting section- Updated project structure