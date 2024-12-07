#Aula 9 Atividade
saldo = [100000]
senha = '123'
for tentativas in range (1,4):
    acesso = input ('Digite sua senha')
    if senha == acesso:
        print ('ACESSO AUTORIZADO')
        operacao = input ('''
             1 - extrato
             2 - saque
             3 - deposito
             
             
             ''')
        if operacao =='1':
            print('R$', saldo)
        elif operacao == '2':
              valor_saque = float(input('Digite o saque:'))
              saldo1 = saldo[0] - valor_saque
              print('R$', saldo1)
        elif operacao == '3':
            valor_deposito = float(input('Digite o deposito:'))
            saldo1 = saldo[0] + valor_deposito
            print('R$',saldo1)
            
            



    else:
        print ('Senha incorreta! Tente novamente')
        if tentativas == 0:
            print('Senha bloqueada!')
            
#Aula 9 teorica foi perdida devido a queda de energia
            
            
            

#MERCARDO
carrinho  =  []
m_valores = []
produtos = ['a','b', 'c']
valores = [10,5,3]
continuar_ = input('Deseja fazer pedido, s/n?')
while continuar_ == 's':
    produto = int(input('add'))
    carrinho.append(produtos[produto])
    m_valores.append(valores[produto])
    print(carrinho)
    s_v = sum(-)
    print('R$', s_v)
    continuar_= input('Continuar - s/n?')
print(carrinho)

#Variaveis globais estão fora de funções
def calcula_imc(altura, peso):
    peso =  float(input('Peso:'))
    altura  =  float(input('Altura: '))
    imc =  peso/altura ** 2
    print('Seu imce é: ', imc)
    if imc < 17:
        print('Muito abaixo do peso')
    elif imc > 17 and imc < 19:
        print('Abaixo do peso')
    elif imc >=18 and imc <=24:
        print('Normal')
    elif imc >= 25 and   imc <= 29.99:
        print('Acima do peso')
    elif imc >= 30 and imc <= 34.99:
         print('Obesidade I')
    else:
        print('Digite algo valido')

        
def system():
    peso = float(input('Peso:'))
    altura = float(input('altura:'))
    
print(altura)

def soma(a,b):
    return a + b

def sub(a,b):
    return a - b


def div(a,b):
    d  =  a / b
    return d
    if b == 0:
        print('Não use zero para dividir')


def mult(a,b):
    return a * b


def calculadora():
    print('CALCULADORA')
    n =  float(input('--'))
    op = input(' + | - | * /')
    if op == '+':
       n2 =  float(input('--'))
       som = soma(n,n2)
       print(som)
    elif op == '-':
       n2 =  float(input('--'))
       su  =  sub(n,n2)
       print(su)
    elif op == '*':
       n2 =  float(input('--'))
       mul  =  mult(n,n2)
       print(mul)       
    elif op == '/':
       n2 =  float(input('--'))
       di  =  div(n,n2)
       print(div)       
    
def loop():
    while True:
        calculadora()
    
    
loop()    

def cumprimento(nome):
    print('seja bem vindo(a)', nome)
    
def operacao(saldo, op):
    
    if op == '1':
        print(saldo)
        
    elif op == '2':
        valor =  float(input('R$: '))
        deposito = saldo + valor
        print(deposito)
    elif op == '3':
        valor =  float(input('R$: '))
        saque = saldo - valor
        print(saque)
        

def banco():
    nome  =  input('Nome:')
    cumprimento(nome)
    saldo  =  20000
    op = input('Operação: ')
    operacao(saldo, op)
    print('Obrigada volte sempre!!!')
    
while True:
      banco()
    
    