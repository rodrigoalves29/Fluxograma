import statistics

def moda(lista):
    moda = statistics.mode(lista)
    print('moda', moda)

def media(lista):
    media = statistics.mean(lista)
    print('media', media)

def mediana(lista):
    mediana = statistics.median(lista)
    print('mediana',mediana)

def desvio(lista):
    desvio = statistics.stdev(lista)
    print("Desvio:", desvio) 


def display():
    print('Empresa 1')
    empresa1 = [1000,6000,1200,8000,1400]
    desvio(empresa1)
    moda(empresa1)
    mediana(empresa1)
    media(empresa1) 

    print('--------------------------')  

    print('Empresa 2')
    empresa2 = [5000,4000,3000,2000,7000]
    desvio(empresa2)
    moda(empresa2)
    mediana(empresa2)
    media(empresa2) 

    print('--------------------------') 

    print('Empresa 3')
    empresa3 = [1200,1300,8000,3000,15000]
    desvio(empresa3)
    moda(empresa3)
    mediana(empresa3)
    media(empresa3) 

    print('--------------------------')

    print('Empresa 4')
    empresa4 = [1400,1750,2000,4500,5900]
    desvio(empresa4)
    moda(empresa4)
    mediana(empresa4)
    media(empresa4) 
    
    print('--------------------------')        
            
    
display()
