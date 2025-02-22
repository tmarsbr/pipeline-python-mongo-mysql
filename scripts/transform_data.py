import pandas as pd
from typing import List, Dict, Any
from extract_and_save_data import connect_mongo, create_connect_db, create_connect_collection
import os
from pathlib import Path

def visualize_collection(collection):
    """Imprime todos os documentos na coleção"""
    for doc in collection.find():
        print(doc)

def rename_column(collection, col_name: str, new_name: str):
    """Renomeia uma coluna na coleção"""
    collection.update_many({}, {"$rename": {col_name: new_name}})

def select_category(collection, category: str) -> List[Dict]:
    """Seleciona documentos por categoria"""
    query = {"Categoria do Produto": category}
    return list(collection.find(query))

def make_regex(collection, regex: str) -> List[Dict]:
    """Seleciona documentos por regex na data"""
    query = {"Data da Compra": {"$regex": regex}}
    return list(collection.find(query))

def create_dataframe(data: List[Dict]) -> pd.DataFrame:
    """Cria DataFrame pandas"""
    return pd.DataFrame(data)

def format_date(df: pd.DataFrame) -> pd.DataFrame:
    """Formata coluna de data para ano-mes-dia"""
    df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], format="%d/%m/%Y")
    df["Data da Compra"] = df["Data da Compra"].dt.strftime("%Y-%m-%d")
    return df

def save_csv(df: pd.DataFrame, path: str):
    """Salva DataFrame como CSV"""
    # Garantir que o diretório existe
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Arquivo salvo em: {path}")

def main():
    # Configurações
    MONGO_URI = "mongodb+srv://tmars:13931p12K@cluster-pipeline.zz7e2.mongodb.net/?retryWrites=true&w=majority"
    DB_NAME = "db_produtos"
    COLLECTION_NAME = "produtos"

    # Define caminhos absolutos para arquivos CSV
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"
    
    # Conexão
    client = connect_mongo(MONGO_URI)
    db = create_connect_db(client, DB_NAME)
    collection = create_connect_collection(db, COLLECTION_NAME)

    try:
        # Renomear colunas
        rename_column(collection, "lat", "Latitude")
        rename_column(collection, "lon", "Longitude")

        # Processar categoria livros
        livros = select_category(collection, "livros")
        df_livros = create_dataframe(livros)
        df_livros = format_date(df_livros)
        save_csv(df_livros, str(DATA_DIR / "tabela_livros.csv"))

        # Processar vendas a partir de 2021
        vendas_2021 = make_regex(collection, "/202[1-9]")
        df_vendas = create_dataframe(vendas_2021)
        df_vendas = format_date(df_vendas)
        save_csv(df_vendas, str(DATA_DIR / "tabela_produtos_2021.csv"))

    finally:
        client.close()

if __name__ == "__main__":
    main()
