# Pipeline Python - MongoDB - MySQL

Pipeline de dados para empresa de e-commerce integrando Python, MongoDB e MySQL.

## Descrição

Este projeto implementa um pipeline de dados que:
1. Extrai dados de produtos de uma API
2. Armazena dados brutos no MongoDB
3. Transforma os dados conforme necessário
4. Gera arquivos CSV para análise

## Pré-requisitos

- Python 3.8+
- MongoDB Atlas conta
- pip (gerenciador de pacotes Python)

## Dependências

O projeto utiliza as seguintes bibliotecas Python:
- requests 2.31.0: Para requisições HTTP à API
- pymongo 4.4.0: Para conexão com MongoDB
- pandas 2.0.3: Para manipulação de dados
- mysql-connector-python 8.0.33: Para conexão com MySQL (futura implementação)
- python-dotenv: Para gerenciamento de variáveis de ambiente
- numpy 1.24.3: Para operações numéricas

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

## Configuração

### MongoDB Atlas

1. Crie uma conta no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Crie um novo cluster (gratuito)
3. Configure o acesso ao banco:
   - Em "Security" > "Database Access", crie um usuário
   - Em "Security" > "Network Access", adicione seu IP
4. Obtenha a string de conexão:
   - Vá para "Databases" > "Connect"
   - Escolha "Connect your application"
   - Copie a string de conexão

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com:

```
MONGODB_URI=sua_string_conexao_atlas
MONGODB_DB=db_produtos
API_BASE_URL=https://labdados.com/produtos
```

## Uso

O pipeline consiste em dois scripts principais:

### 1. Extração de Dados (extract_and_save_data.py)
```bash
python scripts/extract_and_save_data.py
```
- Conecta à API
- Extrai dados
- Salva no MongoDB

### 2. Transformação de Dados (transform_data.py)
```bash
python scripts/transform_data.py
```
- Lê dados do MongoDB
- Aplica transformações
- Gera arquivos CSV em /data

## Estrutura do Projeto

```
pipeline-python-mongo-mysql/
├── data/                    # Diretório para arquivos CSV gerados
├── notebooks/              # Jupyter notebooks para desenvolvimento
├── scripts/               # Scripts Python do pipeline
│   ├── extract_and_save_data.py
│   └── transform_data.py
├── requirements.txt       # Dependências do projeto
└── README.md             # Documentação
```

## Arquivos CSV Gerados

O pipeline gera dois arquivos CSV:
- `data/tabela_livros.csv`: Produtos da categoria livros
- `data/tabela_produtos_2021.csv`: Vendas a partir de 2021

## Contribuição

1. Fork o projeto
2. Crie sua branch de feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request
