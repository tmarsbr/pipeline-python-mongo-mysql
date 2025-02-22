# %% [markdown]
# Realizando a conexao com o mongoDB
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

# %% [markdown]
# Criando a base de dados e a coleção
# %%
db = client["db_produtos"]
collection = db["produtos"]

# %% 
client.list_database_names()
# %%
product = {
    "product_id": "123",
    "name": "Smartphone",
    "price": 1999.99,
    "category": "Eletronics"
}
collection.insert_one(product)
# %% 
collection.find_one()
# %% [markdown]
# Extrindo os dados da API
# %%
import requests

# %%
reponse = requests.get("https://labdados.com/produtos")
reponse.json()
# %%
len(reponse.json())
# %% [markdown]
# adicionando os dados extraidos na coleção
# %%
docs  = collection.insert_many(reponse.json())
# %% 
len(docs.inserted_ids)
# %% 
collection.count_documents({})
# %%
client.close()
# %%
