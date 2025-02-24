# %% [markdown]
# Configurando mysql com python 
# %%
import mysql.connector

cnx = mysql.connector.connect(
    host='localhost', 
    user='tmars', 
    password='13931',
)
print(cnx)
# %%
cursor = cnx.cursor()

# %%
cursor.execute('CREATE DATABASE IF NOT EXISTS dbprodutos;')
# %%
cursor.execute('SHOW DATABASES;')

for db in cursor:
    print(db)
# %% [markdown] 
# criando uma tabela 
# %%
import pandas as pd 
# %%
df_livros  = pd.read_csv('../data/tabela_livros.csv')
df_livros.shape 
# %%
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dbprodutos.tb_livros (
       id VARCHAR(100),
        Produto VARCHAR(100),
        Categoria_Produto VARCHAR(100),
        Preco FLOAT(10,2),
        Frete FLOAT(10,2),
        Data_Compra DATE,
        Vendedor VARCHAR(100),
        Local_Compra VARCHAR(100),
        Avaliacao_Compra INT,
        Tipo_Pagamento VARCHAR(100),
        Qntd_Parcelas INT,
        Latitude FLOAT(10,2),
        Longitude FLOAT(10,2),
        
        PRIMARY KEY (id)
    );
""")
# %%
cursor.execute('USE dbprodutos;')
cursor.execute('SHOW TABLES;')
for table in cursor:
    print(table)
# %% [markdown]
# Inserindo dados na tabela
# %%
for i, row in df_livros.iterrows():
    print(tuple(row))

# %%
lista_dados = [tuple(row) for i, row in df_livros.iterrows()]
lista_dados
# %%
sql = "INSERT INTO dbprodutos.tb_livros  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

cursor.executemany(sql, lista_dados)
cnx.commit()
# %%
print(cursor.rowcount, "registro(s) inserido(s).")
# %% 
# Fechando a conexão
cursor.close()
cnx.close()
# %%