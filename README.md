<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="_API_de_Catlogo_de_Veculos_0"></a>🚗 API de Catálogo de Veículos</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">API REST para gerenciamento de catálogo de veículos, desenvolvida com Flask e MongoDB Atlas. Sistema completo de autenticação e operações CRUD para veículos.</p>
<h2 class="code-line" data-line-start=4 data-line-end=5 ><a id="_ndice_4"></a>📋 Índice</h2>
<ul>
<li class="has-line-data" data-line-start="5" data-line-end="6"><a href="#-tecnologias">Tecnologias</a></li>
<li class="has-line-data" data-line-start="6" data-line-end="7"><a href="#-estrutura-do-projeto">Estrutura do Projeto</a></li>
<li class="has-line-data" data-line-start="7" data-line-end="8"><a href="#-instala%C3%A7%C3%A3o">Instalação</a></li>
<li class="has-line-data" data-line-start="8" data-line-end="9"><a href="#-configura%C3%A7%C3%A3o">Configuração</a></li>
<li class="has-line-data" data-line-start="9" data-line-end="10"><a href="#-uso">Uso</a></li>
<li class="has-line-data" data-line-start="10" data-line-end="11"><a href="#-endpoints">Endpoints</a></li>
<li class="has-line-data" data-line-start="11" data-line-end="12"><a href="#-testes">Testes</a></li>
<li class="has-line-data" data-line-start="12" data-line-end="14"><a href="#-solu%C3%A7%C3%A3o-de-problemas">Solução de Problemas</a></li>
</ul>
<h2 class="code-line" data-line-start=14 data-line-end=15 ><a id="_Tecnologias_14"></a>🚀 Tecnologias</h2>
<ul>
<li class="has-line-data" data-line-start="16" data-line-end="17"><strong>Backend:</strong> Python 3.x, Flask</li>
<li class="has-line-data" data-line-start="17" data-line-end="18"><strong>Banco de Dados:</strong> MongoDB Atlas</li>
<li class="has-line-data" data-line-start="18" data-line-end="19"><strong>Autenticação:</strong> Flask-JWT-Extended</li>
<li class="has-line-data" data-line-start="19" data-line-end="24"><strong>Bibliotecas:</strong>
<ul>
<li class="has-line-data" data-line-start="20" data-line-end="21">Flask-PyMongo</li>
<li class="has-line-data" data-line-start="21" data-line-end="22">Python-dotenv</li>
<li class="has-line-data" data-line-start="22" data-line-end="24">Werkzeug</li>
</ul>
</li>
</ul>
<h2 class="code-line" data-line-start=24 data-line-end=25 ><a id="_Estrutura_do_Projeto_24"></a>📁 Estrutura do Projeto</h2>
<p class="has-line-data" data-line-start="25" data-line-end="36">api-catalogos-de-carros/<br>
├── app/<br>
├── <a href="http://init.py">init.py</a> # Configuração da aplicação │<br>
├── <a href="http://extensions.py">extensions.py</a> # Extensões Flask │<br>
└── routes/<br>
├── <a href="http://auth.py">auth.py</a> # Rotas de autenticação<br>
└── <a href="http://vehicles.py">vehicles.py</a> # Rotas de veículos<br>
├── .env # Variáveis de ambiente<br>
├── .gitignore<br>
├── requirements.txt # Dependências<br>
└── <a href="http://run.py">run.py</a> # Arquivo principal</p>
<p class="has-line-data" data-line-start="37" data-line-end="38">plaintext</p>
<h2 class="code-line" data-line-start=39 data-line-end=40 ><a id="_Instalao1_Clone_o_repositrio_httpsgithubcomseuusuarioapicatalogosdecarrosgitcd_apicatalogosdecarros_39"></a>🔧 Instalação1. <strong>Clone o repositório:</strong> <a href="https://github.com/seu-usuario/api-catalogos-de-carros.gitcd">https://github.com/seu-usuario/api-catalogos-de-carros.gitcd</a> api-catalogos-de-carros</h2>
<p class="has-line-data" data-line-start="40" data-line-end="43">Crie e ative o ambiente virtual:<br>
Run<br>
python -m venv venvvenv\Scripts\activate</p>
<p class="has-line-data" data-line-start="44" data-line-end="47">Instale as dependências:<br>
bash<br>
pip install -r requirements.txt</p>
<p class="has-line-data" data-line-start="48" data-line-end="50">⚙️ Configuração<br>
Configure o MongoDB Atlas:</p>
<p class="has-line-data" data-line-start="51" data-line-end="56">Crie uma conta no MongoDB Atlas<br>
Configure um novo cluster<br>
Obtenha a URI de conexão<br>
Libere o IP no MongoDB Atlas<br>
Configure o arquivo .env:</p>
<p class="has-line-data" data-line-start="57" data-line-end="59">env<br>
MONGO_URI=mongodb+srv://seu_usuario:sua_senha@seu_cluster.mongodb.net/vehicles_dbJWT_SECRET_KEY=sua_chave_jwt_secreta</p>
<p class="has-line-data" data-line-start="60" data-line-end="65">🏃‍♂️ Uso<br>
Execute a aplicação:<br>
bash<br>
Run<br>
python <a href="http://run.py">run.py</a></p>
<p class="has-line-data" data-line-start="66" data-line-end="76">Acesse a API: <a href="http://localhost:5000">http://localhost:5000</a><br>
🛣️ Endpoints<br>
Autenticação<br>
Método  Rota    Descrição<br>
POST<br>
/login<br>
Login do usuário<br>
Exemp<br>
json<br>
{    “username”: “admin”,    “password”: “sua_senha”}</p>
<p class="has-line-data" data-line-start="77" data-line-end="82">Veículos<br>
Método  Rota    Descrição   Auth<br>
GET<br>
/vehicles<br>
Lista todos os veículos</p>
<p class="has-line-data" data-line-start="83" data-line-end="86">GET<br>
/vehicles/&lt;id&gt;<br>
Obtém um veículo</p>
<p class="has-line-data" data-line-start="87" data-line-end="90">POST<br>
/admin/vehicles<br>
Cria veículo</p>
<p class="has-line-data" data-line-start="91" data-line-end="94">PUT<br>
/admin/vehicles/&lt;id&gt;<br>
Atualiza veículo</p>
<p class="has-line-data" data-line-start="95" data-line-end="98">DELETE<br>
/admin/vehicles/&lt;id&gt;<br>
Remove veículo</p>
<p class="has-line-data" data-line-start="99" data-line-end="100">Exemplo de Veículo:</p>
<p class="has-line-data" data-line-start="101" data-line-end="102">{    “nome”: “Civic”,    “marca”: “Honda”,    “modelo”: “EXL”,    “foto”: “url_da_foto”,    “valor”: 150000.00}</p>
<p class="has-line-data" data-line-start="103" data-line-end="104">🧪 Testes com Insomnia</p>
<ol>
<li class="has-line-data" data-line-start="104" data-line-end="108">Login (obter token)<br>
Método: POST<br>
URL: <a href="http://localhost:5000/login">http://localhost:5000/login</a></li>
</ol>
<p class="has-line-data" data-line-start="108" data-line-end="113">Headers:<br>
Content-Type: application/json<br>
Body:<br>
json<br>
{    “username”: “admin”,    “password”: “sua_senha”}</p>
<ol start="2">
<li class="has-line-data" data-line-start="114" data-line-end="121">Criar Veículo<br>
Método: POST<br>
URL: <a href="http://localhost:5000/admin/vehicles">http://localhost:5000/admin/vehicles</a><br>
Headers:<br>
plaintext<br>
Content-Type: application/jsonAuthorization: Bearer seu_token_jwt</li>
</ol>
<p class="has-line-data" data-line-start="121" data-line-end="124">Body:<br>
json<br>
{    “nome”: “Civic”,    “marca”: “Honda”,    “modelo”: “EXL”,    “foto”: “url_da_foto”,    “valor”: 150000.00}</p>
<p class="has-line-data" data-line-start="125" data-line-end="131">🔧 Solução de Problemas<br>
Erro de Conexão MongoDB (500)<br>
✔️ Soluções:<br>
Verifique a URI do MongoDB no arquivo .env<br>
Confirme se o IP está liberado no MongoDB Atlas<br>
Verifique as credenciais de acesso</p>
<p class="has-line-data" data-line-start="132" data-line-end="138">Erro de Autenticação (401/422)<br>
✔️ Soluções:<br>
Certifique-se de incluir o token JWT<br>
Use o prefixo “Bearer” no token<br>
Verifique se o token não está expirado<br>
Erro ao Criar Veículo (400)</p>
<p class="has-line-data" data-line-start="139" data-line-end="143">✔️ Soluções:<br>
Verifique se todos os campos obrigatórios estão presentes<br>
Confirme o formato correto do JSON<br>
Verifique a conexão com o banco de dados</p>
<p class="has-line-data" data-line-start="144" data-line-end="154">🛠️ Desenvolvimento<br>
Requisitos para Contribuir<br>
Conhecimento em Python e Flask<br>
Familiaridade com MongoDB<br>
Entendimento de autenticação JWT<br>
Boas Práticas<br>
Siga o padrão PEP 8<br>
Documente novas funcionalidades<br>
Teste todas as alterações<br>
Mantenha o código limpo e organizado</p>
<p class="has-line-data" data-line-start="155" data-line-end="162">📈 Melhorias Futuras<br>
Implementar cache para otimização<br>
Adicionar sistema de logs<br>
Implementar testes automatizados<br>
Adicionar documentação Swagger<br>
Implementar sistema de refresh token<br>
Adicionar validação de dados avançada</p>
<p class="has-line-data" data-line-start="163" data-line-end="165">📄 Licença<br>
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.</p>
<p class="has-line-data" data-line-start="166" data-line-end="170">👥 Autores<br>
Desenvolvedor Principal - Seu Nome<br>
📞 Suporte<br>
Para suporte, envie um email para <a href="mailto:seu@email.com">seu@email.com</a> ou abra uma issue no repositório.</p>
<p class="has-line-data" data-line-start="171" data-line-end="173">plaintext<br>
As adições incluem:- Seção de desenvolvimento- Boas práticas- Melhorias futuras planejadas- Informações sobre autores- Seção de suporte- Requisitos para contribuição</p>
