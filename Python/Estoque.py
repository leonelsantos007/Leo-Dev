import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conexão com o banco de dados
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Criação da tabela de estoque
cursor.execute('''
CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
)
''')
conn.commit()

# Funções para o sistema
def adicionar_produto():
    produto = entry_produto.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()
    if produto and quantidade and preco:
        cursor.execute('''
        INSERT INTO estoque (produto, quantidade, preco)
        VALUES (?, ?, ?)
        ''', (produto, quantidade, preco))
        conn.commit()
        entry_produto.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        messagebox.showinfo('Sucesso', 'Produto adicionado com sucesso!')
    else:
        messagebox.showwarning('Atenção', 'Todos os campos são obrigatórios!')

def visualizar_estoque():
    cursor.execute('SELECT * FROM estoque')
    rows = cursor.fetchall()
    produtos = pd.DataFrame(rows, columns=['ID', 'Produto', 'Quantidade', 'Preço'])
    print(produtos)

def gerar_relatorio():
    cursor.execute('SELECT * FROM estoque')
    rows = cursor.fetchall()
    produtos = pd.DataFrame(rows, columns=['ID', 'Produto', 'Quantidade', 'Preço'])
    produtos.plot(kind='bar', x='Produto', y='Quantidade')
    plt.xlabel('Produto')
    plt.ylabel('Quantidade')
    plt.title('Relatório de Estoque')
    plt.show()

# Configuração da janela principal
root = tk.Tk()
root.title('Sistema de Gerenciamento de Estoque')

# Widgets de entrada
tk.Label(root, text='Produto').grid(row=0, column=0)
entry_produto = tk.Entry(root)
entry_produto.grid(row=0, column=1)

tk.Label(root, text='Quantidade').grid(row=1, column=0)
entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=1, column=1)

tk.Label(root, text='Preço').grid(row=2, column=0)
entry_preco = tk.Entry(root)
entry_preco.grid(row=2, column=1)

# Botões
tk.Button(root, text='Adicionar Produto', command=adicionar_produto).grid(row=3, column=0, columnspan=2)
tk.Button(root, text='Visualizar Estoque', command=visualizar_estoque).grid(row=4, column=0, columnspan=2)
tk.Button(root, text='Gerar Relatório', command=gerar_relatorio).grid(row=5, column=0, columnspan=2)

root.mainloop()

# Fechar a conexão com o banco de dados ao encerrar
conn.close()
