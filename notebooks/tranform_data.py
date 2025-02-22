# %% [markdown]
# Realizando conexão com o MongoDB
# %% 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://tmars:13931p12K@cluster-pipeline.zz7e2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-pipeline"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# %%
db = client['db_produtos']
collection = db['produtos']

# %%
for doc in collection.find():
    print(doc)
# %%
collection.update_many({}, {"$rename": {"lat": "latitude", "lon": "longitude"}})
# %%
collection.find_one()
# %% [markdown]
# Aplicando transformações: filtrando registros da categoria livros
# %%
collection.distinct('Categoria do Produto')

# %%


query = {"Categoria do Produto": "livros"}

lista_livros = []

livros = collection.find(query)
for livro in livros:
    lista_livros.append(livro)
# %% 
lista_livros
# %% [markdown]

# Salvando os dados em um dataframe

# %%
import pandas as pd
# %%

df_livros = pd.DataFrame(lista_livros)
df_livros.head()

# %% [markdown]
# Formatando os datas
# %%
df_livros.info()
# %%
df_livros["Data da Compra"] = pd.to_datetime(df_livros["Data da Compra"], format="%d/%m/%Y")
df_livros.info()
# %%
df_livros["Data da Compra"] = df_livros["Data da Compra"].dt.strftime("%Y-%m-%d")
# %%
df_livros.head()
# %% [markdown]
# Salvando os dados em csv
# %%)
df_livros.to_csv("../data/tabela_livros.csv", index=False)
# %%
# %% [markdown]

# Aplicando transformaçoes: filtrando produtos vendidos a partir de 2021

# %%
collection.find_one()
# %%
query = {"Data da Compra": {"$regex": "/202[1-9]"}}

lista_produtos = []

for doc in collection.find(query):
    lista_produtos.append(doc)
# %%
df_produtos = pd.DataFrame(lista_produtos)
df_produtos.head()
# %%
df_produtos["Data da Compra"] = pd.to_datetime(df_produtos["Data da Compra"], format="%d/%m/%Y")
df_produtos["Data da Compra"] = df_produtos["Data da Compra"].dt.strftime("%Y-%m-%d")
df_produtos.head()
# %%
df_produtos.to_csv("../data/tabela_produtos_2021.csv", index=False)
# %%
client.close()
# %%
