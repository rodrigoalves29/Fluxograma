n = int(input('Digite um número: '))

match n:
    case x if x % 2 == 0:
        print('O número digitado é par.')
    case _:
        print('O número digitado é ímpar.')

x = float(input('Digite um número: '))

match x:
    case 0:
        print('O número digitado é o zero.')
    case x if x > 0:
        print('O número digitado é positivo.')
    case _:
        print('O número digitado é negativo.')

texto = {}

match texto:
    case str(): 
        print('A string não está vazia.')
    case _:
        print('A string está vazia.')

y = 11

match y:
    case y if y > 10:
        print('O número é maior que 10.')
    case y if y < 10:
        print('O número é menor que 10.')
    case _:
        print('O número é igual a 10.')

idade = int(input('Digite sua idade: '))

match idade:
    case idade if idade >= 60:
        print('Você é um idoso.')
    case idade if idade < 60 and idade > 29:
        print('Você é um adulto.')
    case idade if idade < 30 and idade > 14:
        print('Você é um jovem.')
    case idade if idade > -1 and idade < 15:
        print('Você é uma criança.')
    case _:
        print('O valor digitado não condiz com a realidade.')
