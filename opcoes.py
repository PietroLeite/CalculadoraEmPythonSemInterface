import calculos


def menul():
    print("Informe os numeros")
    x = int(input("Informe um Numero: "))
    y = int(input("Informe um Numero: "))
    print(f'Numeros escolhidos foram: {x} e {y}')
    print("Sair: 0 | Soma: 1| Subtração: 2| Divisão: 3| Multiplicação: 4 | 5: Escolher novos numeros")
    while True:
        opcao = int(input("Informe a operaçao que deseja fazer: "))
        if opcao == 1:
            calculos.sum(x, y)
        elif opcao == 2:
            calculos.sub(x, y)
        elif opcao == 3:
            calculos.division(x, y)
        elif opcao == 4:
            calculos.multi(x, y)
        elif opcao == 0:
            print("Saindo!")
            break
        elif opcao == 5:
            x = 0
            y = 0
            x = int(input("Informe um Numero: "))
            y = int(input("Informe um Numero: "))
            print(f'Novos numeros escolhidos foram: {x} e {y}')
        else:
            print("opcao invalida")
