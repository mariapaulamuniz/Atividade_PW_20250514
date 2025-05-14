from data.produto_model import Categoria
from data.produto_sql import *
from data.util import get_connection

def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA)
    conn.commit()
    conn.close()

def inserir(categoria: Categoria):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR, (
        categoria.id,
        categoria.nome))
    conn.commit()
    conn.close()

def obter_todos() -> list[Categoria]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_TODOS)
    tuplas = cursor.fetchall()
    produtos = [
        Categoria(
            id=tupla[0], 
            nome=tupla[1],) 
            for tupla in tuplas]
    conn.close()
    return Categoria