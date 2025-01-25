import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# conectar ou criar banco
def conectar():
    return sqlite3.connect('usuarios.db')

# criar tabela se ela não existir
def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS cliente(
              id INTEGER PRIMARY KEY,
              nome TEXT,
              idade INTEGER,
              EMAIL TEXT,
              TELEFONE INTEGER,
              ENDEREÇO TEXT
              )
              ''')
    conn.commit()
    conn.close()

def agregar_cliente():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereço = entry_endereço.get()

    if nome and idade and email and telefone and endereço:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(nome,idade) VALUES(?,?)' , (nome, idade, email, telefone, endereço))
        conn.commit()
        conn.close()
        messagebox.showinfo('Inseridos', 'Os dados estão no banco de dados')
        mostrar_cliente()
    else:
        messagebox.showerror('Erro', 'Ocorreu um erro os dados não foram inseridos')

# mostrar dados
def mostrar_cliente():
    for row in tree.get_children():
        tree.delee(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * from cliente')
    cliente = c.fetchall()
    for usuario in cliente:
        tree.insert("","end", values=(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4]))
    conn.close()

#deletar dados
def eliminar_cliente():
    selected = tree.selection()
    if selected:
        user_id = tree.item(selected['values'][0])
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ?', (user_id))
        conn.commit()
        conn.close()
        messagebox.showinfo('Exito','DADOS DELETADOS')
        mostrar_cliente()
    else:
        messagebox.showerror('Erro', 'DADOS NÃO DELETADOS')

def atualizar_cliente():
    selected = tree.selection()
    if selected:
        user_id = tree.item(selected)['values'][0]
        novo_nome = entry_nome.get()
        nova_idade = entry_idade.get()
        novo_email = entry_email.get()
        novo_telefone = entry_telefone.get()
        novo_endereço = entry_endereço.get()
        if nova_idade and novo_nome:
            conn = conectar()
            c = conn.cursor()
            c.execute('UPDATE clinte SET nome = ?, WHERE id = ?',
                      (novo_nome, nova_idade, novo_email, novo_telefone, novo_endereço, user_id))
            conn.commit()
            conn.close()
            messagebox.showinfo('Exito', 'dados alterados')
            mostrar_cliente()
        else:
            messagebox.showerror('erro', 'dados não inseridos')
    else:
        messagebox.showerror('Atenção', 'O dado não foi selecionado')

janela = tk.Tk()
janela. title('CRUD USUARIOS')

label_nome = tk.Label(janela, text = 'NOME')
label_nome.grid(row=0, column=0,padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = tk.Label(janela, text = 'IDADE')
label_idade.grid(row=1, column=0,padx=10, pady=10)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(janela, text = 'EMAIL')
label_email.grid(row=2, column=0,padx=10, pady=10)
entry_email = tk.Entry(janela)
entry_email.grid(row=2, column=1, padx=10, pady=10)

label_telefone = tk.Label(janela, text = 'TELEFONE')
label_telefone.grid(row=3, column=0,padx=10, pady=10)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

label_endereço = tk.Label(janela, text = 'ENDEREÇO')
label_endereço.grid(row=4, column=0,padx=10, pady=10)
entry_endereço = tk.Entry(janela)
entry_endereço.grid(row=4, column=1, padx=10, pady=10)

btn_agregar = tk.Button(janela, text = 'INSERIR DADOS', command=agregar_cliente)
btn_agregar.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

btn_atualizar= tk.Button(janela, text = 'ATUALIZAR DADOS', command=atualizar_cliente)
btn_atualizar.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

btn_deletar = tk.Button(janela, text = 'DELETAR DADOS', command=eliminar_cliente)
btn_deletar.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

columns = ('ID', 'NOME', 'IDADE', 'EMAIL', 'TELEFONE', 'ENDEREÇO')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_cliente()

janela.mainloop()