import sqlite3
import pandas as pd

def inicializar_bd():
    with sqlite3.connect("db/natacao.db") as conn:
        with open("db/init.sql", "r") as f:
            conn.executescript(f.read())

def inserir_dataframe(df, tabela):
    with sqlite3.connect("db/natacao.db") as conn:
        df.to_sql(tabela, conn, if_exists='append', index=False)

def obter_dados(tabela, query=None):
    if query:
        with sqlite3.connect("db/natacao.db") as conn:
            return pd.read_sql_query(query, conn)
    else:
        query = f"SELECT * FROM {tabela}"
        return pd.read_sql_query(query, conn)
    
def reset_db():
    with sqlite3.connect("db/natacao.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS atletas")
        cursor.execute("DROP TABLE IF EXISTS eventos")
        cursor.execute("DROP TABLE IF EXISTS resultados")
        conn.commit()
    inicializar_bd()