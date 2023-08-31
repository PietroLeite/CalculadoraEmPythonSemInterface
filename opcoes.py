import calculos


def menul():
    print("Informe os numeros")
    x = int(input("Informe um Numero: "))
    y = int(input("Informe um Numero: "))
    print(f'Numeros escolhidos foram: {x} e {y}')
    print("Sair: 0 | Soma: 1| Subtração: 2| Divisão: 3| Multiplicação: 4 | 5: Escolher novos numeros")
    while True:
        opcao = int(input("Informe a operaçao que deseja fazer: "))
        match opcao:
            case 0:
                print("Saindo!")
                break
            case 1:
                calculos.sum(x, y)
            case 2:
                calculos.sub(x, y)
            case 3:
                calculos.division(x, y)
            case 4:
                calculos.multi(x, y)
            case 5:
                x = int(input("Informe um Numero: "))
                y = int(input("Informe um Numero: "))
                print(f'Novos numeros escolhidos foram: {x} e {y}')
            case _:
                print("opcao invalida")
