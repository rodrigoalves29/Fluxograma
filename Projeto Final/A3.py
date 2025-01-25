import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# conectar ou criar o banco 
def conectar():
    return sqlite3.connect('usuarios.db')

# criar tabela se ela não existir
def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute(''' 
      CREATE TABLE IF NOT EXISTS usuarios(
             id INTEGER PRIMARY KEY,
             nome TEXT,
             idade INTEGER                
        )
    ''')
    conn.commit()
    conn.close()

# inserindo dados no banco de dados
def agregar_usuarios():
    nome = entry_nome.get()
    idade = entry_idade.get()

    if nome and idade:
       conn = conectar()
       c = conn.cursor()
       c.execute('INSERT INTO usuarios(nome, idade) VALUES(?, ?)', (nome, idade))
       conn.commit()
       conn.close()
       messagebox.showinfo('Inseridos', 'Os dados estão no banco de dados') 
       mostrar_usuarios()
    else:
       messagebox.showerror('Erro', 'Ocorreu um erro, os dados não foram inseridos')

# mostrar dados 
def mostrar_usuarios():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * from usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1], usuario[2]))
    conn.close()

# deletar dados 
def eliminar_usuario():
    selected = tree.selection()
    if selected:
        user_id = tree.item(selected)['values'][0]
        conn = conectar() 
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Exito', 'DADOS DELETADOS')
        mostrar_usuarios()
    else:
        messagebox.showerror('Erro', 'Dados não deletados')

def atualizar_usuario():
    selected = tree.selection()
    if selected:
        user_id = tree.item(selected)['values'][0]
        novo_nome = entry_nome.get()
        nova_idade = entry_idade.get()
        if novo_nome and nova_idade:
            conn = conectar() 
            c = conn.cursor()
            c.execute('UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?', 
                     (novo_nome, nova_idade, user_id)) 
            conn.commit()
            conn.close()
            messagebox.showinfo('Exito', 'Dados alterados')
            mostrar_usuarios()
        else:
            messagebox.showerror('Erro', 'Dados não inseridos')
    else:
        messagebox.showwarning('Atenção', 'O dado não foi selecionado')

janela = tk.Tk()
janela.title('CRUD USUARIOS')

label_nome = tk.Label(janela, text='NOME')
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = tk.Label(janela, text='IDADE')
label_idade.grid(row=1, column=0, padx=10, pady=10)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

btn_agregar = tk.Button(janela, text='INSERIR DADOS', command=agregar_usuarios)
btn_agregar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text='ATUALIZAR DADOS', command=atualizar_usuario)
btn_atualizar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

btn_deletar = tk.Button(janela, text='DELETAR DADOS', command=eliminar_usuario)
btn_deletar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

columns = ('ID', 'NOME', 'IDADE')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuarios()

janela.mainloop()
 
    