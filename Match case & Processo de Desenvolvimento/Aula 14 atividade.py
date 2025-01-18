n = int(inpu('Digite um número'))

match n:
case True:
print('O número é par')
case _:
print('O número é impar')

x = int(input('Digite um número'))
match numero:
case numero if numero == 0:
print('zero')
case numero if numero > 0:
print('positivo')
case numero if numero < 0:
print('negaivo')

palavra = input('Digite')
match palavra:
case 'texto':
print('preenchida')
case _:
print('vazia')

numero = int(input('--'))
match numero:
case numero if numero == 10:
    print('é 10')
case numero if numero > 10:
    print('é maior que 10')
case _:
    print('é menor que 10')

def faixas():
    idade  =  int(input('idade: '))
    match idade:
 case idade if idade >=65: 
    print('idoso')
 case idade if idade <18  : 
    print('Adolecente')
case idade if idade >=18 and idade <= 65:
    print('Jovem/ adulto')  