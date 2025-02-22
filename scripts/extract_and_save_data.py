import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import List, Dict, Any

def connect_mongo(uri: str) -> MongoClient:
    """Estabelece conexão com MongoDB"""
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Conexão com MongoDB estabelecida com sucesso!")
        return client
    except Exception as e:
        print(f"Erro ao conectar com MongoDB: {e}")
        raise

def create_connect_db(client: MongoClient, db_name: str):
    """Cria e conecta ao banco de dados"""
    return client[db_name]

def create_connect_collection(db, col_name: str):
    """Cria e conecta à coleção"""
    return db[col_name]

def extract_api_data(url: str) -> List[Dict[str, Any]]:
    """Extrai dados da API"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro ao extrair dados da API: {e}")
        raise

def insert_data(collection, data: List[Dict[str, Any]]) -> int:
    """Insere dados na coleção"""
    result = collection.insert_many(data)
    return len(result.inserted_ids)

def main():
    # Configurações
    MONGO_URI = "mongodb+srv://tmars:13931p12K@cluster-pipeline.zz7e2.mongodb.net/?retryWrites=true&w=majority"
    API_URL = "https://labdados.com/produtos"
    DB_NAME = "db_produtos"
    COLLECTION_NAME = "produtos"

    # Execução do pipeline
    client = connect_mongo(MONGO_URI)
    db = create_connect_db(client, DB_NAME)
    collection = create_connect_collection(db, COLLECTION_NAME)
    
    data = extract_api_data(API_URL)
    inserted_count = insert_data(collection, data)
    print(f"Foram inseridos {inserted_count} documentos na coleção.")
    
    client.close()

if __name__ == "__main__":
    main()
