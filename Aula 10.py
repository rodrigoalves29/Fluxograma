#Aula 10
from div import divisao
from soma import soma
from sub import subtracao
from mult import multiplicacao



def calculadora():
    n1 = float(input('='))
    escolhe_op = input('+ - * /')
    if escolhe_op == '+':
       n2 = float(input('='))
       soma(n1,n2)
    elif escolhe_op == '-':
         n2 = float(input('='))
         subtracao()  
    elif escolhe_op == '*':
        n2 = float(input('='))
        multiplicacao()
    elif escolhe_op == '/':
        n2 = float(input('='))
        divisao()
    else:
        print('Digite algo válido!')  



calculadora()                     
