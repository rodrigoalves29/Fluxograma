#Aula 7

#LISTAS
lista = [1,2,3,4,5,6]
lista_inteiros = [1,2,3,4,5,6,7,8,9,0]
lista_reais = [2.5,3.8,4.7]
lista_string = ['a','b','texto','l','u']
lista_boleana = [True, False, True, False]
lista_mista = ['texto', 5, True, False,'te', 22222222]

#Funções intrisecas manipulação de lista
lista =[]
lista = list(range(1,11))
print(1)

#Adicionar 1 dado apenas
#append
nome = input('digite seu nome:')
lista =[]
lista.append(10)
lista.append(True)
lista.append(15.5)
print(lista)

lista.extend([10,20,30,40,50,60,70,80,90,nome])
lista +=('tr','ty',5)
lista.insert(0,'True')
print(lista)

lista.append(20)
lista.extend(('t',1,20,4,5,6,7,3,5,23))
lista.insert(1,'x')
del lista[0]
print(lista)

lista = [2,4,5,7,2,5,7,8,4,21,3,5,7]
lista.pop(5)
lista.remove(5)
print(lista)

lista2 = [1,2,4,6,9,10]
print('lista verdadeira', lista2)
copia = lista2.copy()
print('copia', copia)

lista3= [1,2,36,4,6]
indice = lista3.index(36)
if indice == 1:
    print('esta parado no indice 1')
else:
    print('não consta')
print(indice)

lista4 = [1,2,3,6]
menor_numero = min(lista4)
maior_numero = max(lista4)
soma = sum (lista4)
somar = [menor_numero, maior_numero]
print(sum(somar))
print(soma, menor_numero,maior_numero)

#range()
cd = list(range(0,151,10))
print(cd)

#Mercardo
lista_produtos = ['macarrão','feijão','uva','sal']
lista_valores = [2.50,5.00,10.00,5.00]
print('Escolha seus produtos:')
print(lista_produtos)

carrinho = []
meus_valores = []

produto1 = int(input('Digite o produto:'))
produto2 = int(input('Digite o produto:'))
produto3 = int(input('Digite o produto:'))

carrinho += (lista_produtos[produto1],lista_produtos[produto2],lista_produtos[produto3])
meus_valores += (lista_valores[produto1],lista_valores[produto2],lista_valores[produto3])
print('seus produtos',carrinho)
print('valores', meus_valores)
soma = sum(meus_valores)
print('TOTAL')
print('R$',soma)

#mercado
lista_produtos  =  ['macarrão', 'feijão', 'uva', 'sal']
lista_valores = [2.50,5.00,10.00,5.00]
print('Escolha seus produtos: ')
print(lista_produtos)

carrinho = []
meus_valores = []

produto1 = int(input('Digite o produto: '))
produto2 = int(input('Digite o produto: '))
produto3 = int(input('Digite o produto: '))
produto4 = int(input('Digite o produto: '))
produto5 = int(input('Digite o produto: '))
produto6 = int(input('Digite o produto: '))

carrinho += (lista_produtos[produto1], lista_produtos[produto2],lista_produtos[produto3],
             lista_produtos[produto4],lista_produtos[produto5],lista_produtos[produto6])
meus_valores +=(lista_valores[produto1], lista_valores[produto2],lista_valores[produto3],
                lista_valores[produto4],lista_valores[produto5],lista_valores[produto6])

print('SEUS PRODUTOS', carrinho)
print('VALORES', meus_valores)
soma =  sum(meus_valores)
print('===============TOTAL================')
print('R$', soma)

#tupla
tupla = (1,5,5,5,5)

t = tuple(range (1,11))
l = list(range(1,11))
a,b,c,d,e,f,g,h,i,j = l
print(a,b,c,d,e,f,g,h,i,j)
print(t)

comprimento = len (t)
soma = sum(t)
menor = min(t)
maior = max(t)

nome = input('digite seu nome')
cpf = input('digite seu cpf')
e_mail = input('digite seu e-mail')
rg = input('digite seu rg')

dados = []

dados.extend([nome,cpf, e_mail, rg])
dados_imutavel = tuple(dados)

print(dados)

#conjuntos
conjunto = {1,2,3,4,5,6,7,8,9,10}
print(conjunto)

dados1 = [1,2,3]
dados2 = [4,5,6]
dados3 = [7,8,9]
dados4 = [1,4,7]

n1 = set(dados1)
n2 = set(dados2)
n3 = set(dados3)
n4 = set(dados4)

conjunto1 = n1.union(n2)
conujnto2 = n3.union(n4)
conjunto = {1,1,1,2,3,4,5,6,7,8,9}

l =list(conjunto)
print(l)

#dicionarios
#objeto detalhado
#key e value/items
pessoa = {'nome':'Pedro',
          'idade':25,
          'cpf':121326546,
          'rg':1213232}
nome_pessoa = pessoa ['rg']
pessoa['idade'] = 100
print (pessoa)




#Aula 8
#Condicionais - condição
idade = int(input('digite sua idade'))

if idade == 20:
    print ('voce tem 20 anos')
else:
    print('voce tem mais de 20 anos')
    
if 10 < 2:
    print('10 é maior')
else:
    print('10 é menor')
    
numero = [10,20,30,40,50,60,70,80,90]
if numero in lista:
    print('existe')
    lista.index (numero)
    print("ele está no indice", indice)
else:
    print('não existe')
    lista.append(numero)
    print (lista)


import random

#lista = ['a','b','c','d']
#aleatorio = random.choose(lista)
#print(aleatorio)
#numero1 = random.randit(1,100)
#numero2 = random.randit(1,100)

print(numero)

import random

print('SISTEMA DA MEGA SENA')

numero_da_sorte1 = random.randrange(1,2)
numero_da_sorte2 = random.randrange(1,2)
numero_da_sorte3 = random.randrange(1,2)
numero_da_sorte4 = random.randrange(1,2)
numero_da_sorte5 = random.randrange(1,2)
numero_da_sorte6 = random.randrange(1,2)

lista_sorteada = [numero_da_sorte1,numero_da_sorte2, numero_da_sorte3, numero_da_sorte4,numero_da_sorte5, numero_da_sorte6]


meu_chute1 = int(input('nº 1'))
meu_chute2 = int(input('nº 2'))
meu_chute3 = int(input('nº 3'))
meu_chute4 = int(input('nº 4'))
meu_chute5 = int(input('nº 5'))
meu_chute6 = int(input('nº 6'))

meus_chutes =  [meu_chute1, meu_chute2, meu_chute3, meu_chute4, meu_chute5, meu_chute6]


if meus_chutes in lista_sorteada:
    print('VOCÊ É O MILINÁRIO DA MEGA DA VIRADA')
else:
    print('Não foi dessa vez')


print(f'''
n°1{numero_da_sorte1}
n°2{numero_da_sorte2}
n°3{numero_da_sorte3}
n°4{numero_da_sorte4}
n°5{numero_da_sorte5}
n°6{numero_da_sorte3}
''')

import random

print('SISTEMA DA MEGA SENA')

numero_da_sorte1 = random.randint(1,60)
print(numero_da_sorte1)
numero_da_sorte2 = random.randint(1,60)
print(numero_da_sorte2)
numero_da_sorte3 = random.randint(1,60)
print(numero_da_sorte3)
numero_da_sorte4 = random.randint(1,60)
print(numero_da_sorte4)
numero_da_sorte5 = random.randint(1,60)
print(numero_da_sorte5)
numero_da_sorte6 = random.randint(1,60)
print(numero_da_sorte6)

lista_sorteada = []

lista_sorteada.append(numero_da_sorte1)
lista_sorteada.append(numero_da_sorte2)
lista_sorteada.append(numero_da_sorte3)
lista_sorteada.append(numero_da_sorte4)
lista_sorteada.append(numero_da_sorte5)
lista_sorteada.append(numero_da_sorte6)
                      


meu_chute1 = int(input('nº 1'))
meu_chute2 = int(input('nº 2'))
meu_chute3 = int(input('nº 3'))
meu_chute4 = int(input('nº 4'))
meu_chute5 = int(input('nº 5'))
meu_chute6 = int(input('nº 6'))




if meu_chute1 and meu_chute2 and meu_chute3 and meu_chute4 and meu_chute5 and meu_chute6 in lista_sorteada:
    print('VOCÊ É O MILINÁRIO DA MEGA DA VIRADA')
elif meu_chute1 or meu_chute2 or meu_chute1 or meu_chute2 or meu_chute3 or meu_chute4 or meu_chute5 or meu_chute6    in lista_sorteada:
    print('Você ganhou R$ 50k') 
else:
    print('Não foi dessa vez')