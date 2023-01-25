menu = """


[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair


=> """

saldo=0
limite = 500
extrato=[]
limites_saques=3
while True:

    opcao=input(menu).upper()

    if opcao=="D":
        leitor=int(input('Digite o valor que deseja depositar: '))
        if leitor>0:
            saldo=saldo+leitor
            extrato.append(f'+{leitor}')
            print('Valor depositado com sucesso')
        else:
            print('Valor Invalido para deposito')
        
    elif opcao=="S":
        leitor=int(input('Digite o valor que deseja sacar: '))
        if (limites_saques>0) and (leitor<=500) and (saldo>leitor):
            saldo=saldo-leitor
            limites_saques= limites_saques-1
            extrato.append(f'-{leitor}')
            print('Valor sacado com sucesso')
        else:
            print('Houve um problema no saque, tente novamente')
        
        if (saldo<leitor):
            print('Saldo insuficiente')

    elif opcao=="E":
        if not extrato:
            print('Nao foram realizadadas movimentações')
        else:
            for i in range(len(extrato)):
                print(f'R$ {extrato[i]}')
            print(f'Saldo atual da conta: {saldo:.2f}')

    elif opcao=='Q':
        break

    else:
        print('Opcão Invalida, digite uma opçao valida')

