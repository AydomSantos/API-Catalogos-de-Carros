# 🚗 API de Catálogo de Veículos

API REST para gerenciamento de catálogo de veículos, desenvolvida com Flask e MongoDB Atlas. Sistema completo de autenticação e operações CRUD para veículos.

## 📋 Índice
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Uso](#-uso)
- [Endpoints](#-endpoints)
- [Testes](#-testes)
- [Solução de Problemas](#-solução-de-problemas)

## 🚀 Tecnologias

- **Backend:** Python 3.x, Flask
- **Banco de Dados:** MongoDB Atlas
- **Autenticação:** Flask-JWT-Extended
- **Bibliotecas:**
  - Flask-PyMongo
  - Python-dotenv
  - Werkzeug

## 📁 Estrutura do Projeto
api-catalogos-de-carros/ 
├── app/ 
    ├── init.py # Configuração da aplicação │ 
    ├── extensions.py # Extensões Flask │ 
    └── routes/ 
      ├── auth.py # Rotas de autenticação 
      └── vehicles.py # Rotas de veículos 
├── .env # Variáveis de ambiente 
├── .gitignore 
├── requirements.txt # Dependências 
└── run.py # Arquivo principal

plaintext

## 🔧 Instalação1. **Clone o repositório:**```bashgit clone https://github.com/seu-usuario/api-catalogos-de-carros.gitcd api-catalogos-de-carros
Crie e ative o ambiente virtual:
bash
Run
python -m venv venvvenv\Scripts\activate

Instale as dependências:
bash
Run
pip install -r requirements.txt

⚙️ Configuração
Configure o MongoDB Atlas:

Crie uma conta no MongoDB Atlas
Configure um novo cluster
Obtenha a URI de conexão
Libere o IP no MongoDB Atlas
Configure o arquivo .env:

env
MONGO_URI=mongodb+srv://seu_usuario:sua_senha@seu_cluster.mongodb.net/vehicles_dbJWT_SECRET_KEY=sua_chave_jwt_secreta
🏃‍♂️ Uso
Execute a aplicação:
bash
Run
python run.py

Acesse a API: http://localhost:5000
🛣️ Endpoints
Autenticação
Método	Rota	Descrição
POST

/login
Login do usuário
Exemp
json
{    "username": "admin",    "password": "sua_senha"}

Veículos
Método	Rota	Descrição	Auth
GET
/vehicles
Lista todos os veículos

GET
/vehicles/<id>
Obtém um veículo

POST
/admin/vehicles
Cria veículo

PUT
/admin/vehicles/<id>
Atualiza veículo

DELETE
/admin/vehicles/<id>
Remove veículo

Exemplo de Veículo:

{    "nome": "Civic",    "marca": "Honda",    "modelo": "EXL",    "foto": "url_da_foto",    "valor": 150000.00}

🧪 Testes com Insomnia
1. Login (obter token)
Método: POST
URL: http://localhost:5000/login

Headers:
Content-Type: application/json
Body:
json
{    "username": "admin",    "password": "sua_senha"}

2. Criar Veículo
Método: POST
URL: http://localhost:5000/admin/vehicles
Headers:
plaintext
Content-Type: application/jsonAuthorization: Bearer seu_token_jwt

Body:
json
{    "nome": "Civic",    "marca": "Honda",    "modelo": "EXL",    "foto": "url_da_foto",    "valor": 150000.00}

🔧 Solução de Problemas
Erro de Conexão MongoDB (500)
✔️ Soluções:
Verifique a URI do MongoDB no arquivo .env
Confirme se o IP está liberado no MongoDB Atlas
Verifique as credenciais de acesso

Erro de Autenticação (401/422)
✔️ Soluções:
Certifique-se de incluir o token JWT
Use o prefixo "Bearer" no token
Verifique se o token não está expirado
Erro ao Criar Veículo (400)

✔️ Soluções:
Verifique se todos os campos obrigatórios estão presentes
Confirme o formato correto do JSON
Verifique a conexão com o banco de dados

🛠️ Desenvolvimento
Requisitos para Contribuir
Conhecimento em Python e Flask
Familiaridade com MongoDB
Entendimento de autenticação JWT
Boas Práticas
Siga o padrão PEP 8
Documente novas funcionalidades
Teste todas as alterações
Mantenha o código limpo e organizado

📈 Melhorias Futuras
Implementar cache para otimização
Adicionar sistema de logs
Implementar testes automatizados
Adicionar documentação Swagger
Implementar sistema de refresh token
Adicionar validação de dados avançada

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

👥 Autores
Desenvolvedor Principal - Seu Nome
📞 Suporte
Para suporte, envie um email para seu@email.com ou abra uma issue no repositório.

plaintext
As adições incluem:- Seção de desenvolvimento- Boas práticas- Melhorias futuras planejadas- Informações sobre autores- Seção de suporte- Requisitos para contribuição




