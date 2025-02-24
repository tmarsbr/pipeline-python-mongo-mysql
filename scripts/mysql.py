import mysql.connector
import pandas as pd

def connect_mysql(host_name, user_name, pw):
    # Estabelece conexão com o MySQL
    return mysql.connector.connect(host=host_name, user=user_name, password=pw)

def create_cursor(cnx):
    # Cria e retorna um cursor para execução de comandos SQL
    return cnx.cursor()

def create_database(cursor, db_name):
    # Cria o banco de dados se não existir
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name};')

def show_databases(cursor):
    # Lista e exibe todos os bancos de dados
    cursor.execute('SHOW DATABASES;')
    for db in cursor:
        print(db)

def create_product_table(cursor, db_name, tb_name):
    # Seleciona o banco de dados e cria a tabela com os campos necessários
    cursor.execute(f'USE {db_name};')
    create_table = f"""
    CREATE TABLE IF NOT EXISTS {tb_name} (
        id VARCHAR(100) PRIMARY KEY,
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
        Longitude FLOAT(10,2)
    );
    """
    cursor.execute(create_table)

def show_tables(cursor, db_name):
    # Seleciona o banco de dados e lista todas as tabelas
    cursor.execute(f'USE {db_name};')
    cursor.execute('SHOW TABLES;')
    for table in cursor:
        print(table)

def read_csv(path):
    # Lê o CSV e retorna um DataFrame do pandas
    return pd.read_csv(path)

def add_product_data(cnx, cursor, df, db_name, tb_name):
    # Insere os dados do DataFrame na tabela especificada
    cursor.execute(f'USE {db_name};')
    sql = "INSERT INTO " + tb_name + " VALUES (" + ", ".join(["%s"] * len(df.columns)) + ");"
    dados = [tuple(row) for row in df.itertuples(index=False)]
    cursor.executemany(sql, dados)
    cnx.commit()

if __name__ == '__main__':
    cnx = connect_mysql('localhost', 'tmars', '13931')
    cursor = create_cursor(cnx)
    
    db_name = "db_produtos_teste"
    tb_name = "tb_livros"
    
    create_database(cursor, db_name)
    show_databases(cursor)
    
    create_product_table(cursor, db_name, tb_name)
    show_tables(cursor, db_name)
    
    df = read_csv('../data/tb_livros.csv')  # ajuste o caminho se necessário
    add_product_data(cnx, cursor, df, db_name, tb_name)
    
    cursor.close()
    cnx.close()