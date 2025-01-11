#Aula 11
#EXC 1
try:
     numero =  int(input('Insira um número: '))
 except TypeError:
     print('Você digitou incorretamente')
 except ValueError:
     print('Você inseriu um tipo de dado incorreto')
 else:
    print(numero)
#EXC2
try:
    x = float(input('Digite um número'))
    y = float(input('Digite outro número'))
 coci = x/y
 except ZeroDivisionError as Erro:
     print('Não é possível dividir por zero')
     else:
         print(coci)
         
#EXC3
lista = [10,2,3,6]
def verificar (lista);
 try:
     indice = int(input)
     dado = lista[indice]
     print(dado)
    except IndexError as erro:
        print(dado)
        