# %% 
import mysql.connector
import pandas as pd

# Conectando ao MySQL
cnx = mysql.connector.connect(
    host='localhost', 
    user='tmars', 
    password='13931'
)
cursor = cnx.cursor()

# Criar o banco de dados se não existir
cursor.execute('CREATE DATABASE IF NOT EXISTS dbprodutos;')

# Selecionar o banco de dados
cursor.execute('USE dbprodutos;')

# Criar a nova tabela tb_produtos_2021
create_table = """
    CREATE TABLE IF NOT EXISTS tb_produtos_2021 (
        _id VARCHAR(100) PRIMARY KEY,
        Produto VARCHAR(100),
        `Categoria do Produto` VARCHAR(100),
        Preço FLOAT(10,2),
        Frete FLOAT(10,2),
        `Data da Compra` DATE,
        Vendedor VARCHAR(100),
        `Local da compra` VARCHAR(100),
        `Avaliação da compra` INT,
        `Tipo de pagamento` VARCHAR(100),
        `Quantidade de parcelas` INT,
        Latitude FLOAT(10,2),
        Longitude FLOAT(10,2)
    );
"""
cursor.execute(create_table)
cnx.commit()

# Ler o CSV de vendas a partir de 2021
df_produtos = pd.read_csv('../data/tabela_produtos_2021.csv')

# Montar os dados para inserção
dados = [tuple(row) for row in df_produtos.itertuples(index=False)]
sql = "INSERT INTO tb_produtos_2021 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
cursor.executemany(sql, dados)
cnx.commit()

print(cursor.rowcount, "registro(s) inserido(s) na tabela tb_produtos_2021.")

cursor.close()
cnx.close()

# %%
