import sqlite3
from pathlib import Path

DB_PATH = Path("swim_sim.db")

def get_connection():
    """Retorna uma conexão à base de dados SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # permite acessar colunas por nome
    return conn