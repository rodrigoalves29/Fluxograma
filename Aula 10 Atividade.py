#Aula 10 Atividade
def atendimento():
    lista_produtos = ('pão', 'café com açúcar', 'café sem açúcar', 'pão na chapa com manteiga',' mortadela', 'presunto', 'muçarela', 'rosquinha')
    print('Seja bem vindo(a) ao padaria do Toninho, fique a vontade em olhar nossas opções.')
    print('''
          1 - 1 pão -> R$ 0,30 cada
          2 - 200 ml de café com açúcar -> R$ 1,50
          3 - 200 ml de café sem açúcar -> R$ 1,25
          4 - 1 pão na chapa com manteiga -> R$ 4,00
          5 - mortadela -> R$ 3,50/100g
          6 - presunto -> R$ 3,50/100g
          7 - muçarela -> R$ 3,50/100g
          8 - 1 rosquinha - R$ 0,50 cada
          ''')
    opcao = int(input('O que você deseja comprar'))
    if opcao == 1:
        qtd = int(input('Quantos pães você vai querer'))
        preco = qtd * 0.30
        print(preco)
    elif opcao == 2:
        qtd = int(input('Quantos copos você vai querer'))
        preco = qtd * 1.5
        print(preco)
    elif opcao == 3:
        qtd = int(input('Quantos copos você vai querer'))
        preco = qtd * 1.25
        print(preco)
    elif opcao == 4:
        qtd = int(input('Quantos pães na chapa você vai querer'))
        preço = qtd * 4
        print(preco)
    elif opcao == 5:
        qtd = int(input('Quantas gramas você vai querer'))
        preco = qtd/1000 * 3.5
        print(preco)
    elif opcao == 6:
        qtd = int(input('Quantas gramas você vai querer'))
        preco = qtd/1000 * 3.5
        print(preco)
    elif opcao == 7:
        qtd = int(input('Quantas gramas você vai querer'))
        preco = qtd/1000 * 3.5
        print(preco)
    elif opcao == 8:
        qtd = int(input('Quantas gramas você vai querer'))
        preco = qtd * 0.5
        print(preco)
continaundo = input('Deseja algo mais?'('Digite S ou N'))
    if continuando == S:
        pedidos()
    else continuando == N:
        
        