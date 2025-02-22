# Pipeline Python - MongoDB - MySQL

Pipeline de dados para empresa de e-commerce integrando Python, MongoDB e MySQL.

## Pré-requisitos

- Python 3.8+
- MongoDB
- MySQL
- pip (gerenciador de pacotes Python)

## Dependências

O projeto utiliza as seguintes bibliotecas Python:
- requests 2.31.0: Para fazer requisições HTTP à API
- pymongo 4.4.0: Para conexão com MongoDB
- pandas 2.0.3: Para manipulação de dados
- mysql-connector-python 8.0.33: Para conexão com MySQL
- python-dotenv: Para gerenciamento de variáveis de ambiente

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração do MongoDB Atlas

1. Crie uma conta no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Crie um novo cluster (gratuito)
3. Configure o acesso ao banco:
   - Em "Security" > "Database Access", crie um usuário
   - Em "Security" > "Network Access", adicione seu IP
4. Obtenha a string de conexão:
   - Vá para "Databases" > "Connect"
   - Escolha "Connect your application"
   - Copie a string de conexão

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com:

```
MONGODB_URI=sua_string_conexao_atlas
MONGODB_DB=ecommerce
API_BASE_URL=url_da_api
MYSQL_HOST=localhost
MYSQL_USER=seu_usuario
MYSQL_PASSWORD=sua_senha
MYSQL_DATABASE=ecommerce
```

## Estrutura do Projeto

```
pipeline-python-mongo-mysql/
├── src/
│   ├── __init__.py
│   ├── mongodb_client.py
│   ├── mysql_client.py
│   └── pipeline.py
├── requirements.txt
└── README.md
```
