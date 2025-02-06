import sqlite3
import os

def conectar():
    conexao = sqlite3.connect('JogoForca.db')
    return conexao

def desconectar(conexao):
     conexao.close()
    

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS SCORE_JOGO(
    id integer primary key autoincrement,
    nome text not null,
    valor_score integer not null
    )""")
    conexao.commit()

def inserir_dado(nome, valor):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(""" insert into score_jogo(nome, valor_score) values(?,?)""", (nome, valor))
    conexao.commit()
    desconectar(conexao)

def listar_dados():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(""" select * from score_jogo order by valor_score desc""")
    dados = cursor.fetchall()
    conexao.commit()
    desconectar(conexao)
    return dados