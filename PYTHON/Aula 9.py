#AULA 9
saldo  =  [10000]
senha  = '123'

escolha =  input('deseja sair/ s/n')
while escolha == 'n':
    acesso  =  input('Digite sua senha')
    if senha  ==  acesso:
        print('ACESSO AUTORIZADO')
        operacao = input('''

                    1 - extrato
                    2 - saque
                    3 - deposito 

          ''')
        if  operacao == '1':
            print('R$', saldo)
            escolha =  input('deseja sair/ s/n')    
        elif operacao == '2':
             valor_saque  =  float(input('Digite o saque: '))
             saldo1  = saldo[0]  - valor_saque
             print('R$', saldo1)
             escolha =  input('deseja sair/ s/n')      
        elif operacao == '3':
             valor_deposito  =  float(input('Digite o deposito: '))
             saldo1  = saldo[0]  + valor_deposito
             print('R$', saldo1)
             escolha =  input('deseja sair/ s/n')     
        
    else:
        print('Senha incorreta... tente novamente')
else:
    print('Obrigada volte sempre')
     
            
#LOOP while
c = 10

while c > 0:
    print(c)
    c = c-1
    
carrinho  =  []
continuar_ = input('s/n?')

while continuar_ == 's':
    produto = input('add')
    carrinho.append(produto)
    print(carrinho)
    continuar_= input('s/n?')
print(carrinho)

