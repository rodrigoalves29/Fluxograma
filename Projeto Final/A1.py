import sqlite3
conexao = sqlite3.connect('meu_banco_de_dados.db')
cursor = conexao.cursor()

# Criar uma tabela
cursor.execute('''
               CRIATE TABLE IF NOT EXISTS pessoas(
               id INTEGER PRIMARY KEY
               AUTOINCREMENT NOT NULL,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL,
               cidade TEXT NOT NULL)
               ''')

# Inserir dados na tabela
nome = input('Digite um nome')
idade = int(input('Digite sua idade'))
cidade = input('Cidade:')
cursor.execute('''
               INSERT INTO pessoas(nome,idade, cidade)
               VALUES(?, ?, ?)
               ''', (nome, idade, cidade))

# Confirmar a transação
conexao.commit()

# Consultar dados da tabela
cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

# Mostrar os dados consultados
for pessoas in pessoas:
    print(f'''ID:{'pessoa'[0]}, Nome:{'pessoa'[1]}, Idade:{'pessoa'[2]}, Cidade:{'pessoa'[3]}''')

# Fechar a conexão
conexao.close() 
