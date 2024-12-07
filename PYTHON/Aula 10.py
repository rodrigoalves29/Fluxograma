#AULA 10 Atividade
#EXC1
def tipo_numero():
    n1 = float(input('Digite um numero'))
    n2 = float(input('Digite um numero'))
    if n1 % 2 == 0 and n2 % 2 == 0:
        print('2 numeros pares')
    elif n1 % 2 == 0 or n2 % 2 == 0:
        print('um par e outro impar')
    else:
        print('2 numeros impares')
        
tipo_numero()
print()

#EXC2
def multiplicacao():
     n1 = int(input('Digite um numero'))
     n2 = int(input('Digite um numero'))
     n3 = int(input('Digite um numero'))
     resultado = n1 * n2 * n3
     print(resultado)
    
multiplicacao()
 
#EXC3
