menu = """


[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
[NU] Cadastras Usuario
[NC] Nova Conta
[LC] Listar Contas


=> """

saldo=0
numero_conta=0
extrato=[]
usuarios=[]
contas=[]
AGENCIA="0001"
LIMITE_SAQUES=3


def depositar(saldo,leitor,extrato, /):
    if leitor>0:
        saldo+=leitor
        extrato.append(f'+ R$ {leitor:.2f}')
        print('Valor depositado com sucesso')
    else:
        print('Valor Invalido para deposito')
    return saldo,extrato

def sacar(*, leitor, saldo, extrato, LIMITE_SAQUES):
    if (LIMITE_SAQUES>0) and (leitor<=500) and (saldo>leitor):
            saldo=saldo-leitor
            LIMITE_SAQUES= LIMITE_SAQUES-1
            extrato.append(f'- R$ {leitor:.2f}')
            print('Valor sacado com sucesso')
    else:
            print('Houve um problema no saque, tente novamente')      
    if (saldo<leitor):
        print('Saldo insuficiente')
    return saldo,extrato,LIMITE_SAQUES

def exibir_extrato(saldo, /, *, extrato):
        if not extrato:
            print('Nao foram realizadadas movimentações')
        else:
            for i in range(len(extrato)):
                print(extrato[i])
            print(f'Saldo atual da conta: {saldo:.2f}')    

def criar_usuario(usuarios):
    cpf= input('Digite seu CPF: ')
    usuario= verifica_usuario(cpf, usuarios)
    if usuario:
        print('Ja existe um ususario com este CPF')
        return

    nome=input('Digite seu nome completo: ')
    data_nascimento = input('Digite sua data de nascimento (DD-MM-AA): ')
    endereco = input('Digite seu endereço: ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco":endereco})
    print('Usuario cadastrado com SUCESSO!')

def verifica_usuario(cpf, usuarios):
    filtra_usuarios = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtra_usuarios[0] if filtra_usuarios else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf= input('Digite seu CPF: ')
    usuario= verifica_usuario(cpf, usuarios)
    
    if usuario:
        print('Conta criada com SUCESSO!')
        return {"agencia":agencia, "numero_conta":numero_conta,"usuario":usuario}
    print('Usuario não encontrado, criação de conta encerrada!')

def listar_contas(contas):
    for conta in contas:
        linha=(f"""
            Agencia:{conta['agencia']}\n
            C/C:{conta['numero_conta']}\n
            Titular:{conta['usuario']['nome']}\n
        """)
        print("="*30)
        print(linha)

while True:

    opcao=input(menu).upper()

    if opcao=="D":
        leitor=float(input('Digite o valor que deseja depositar: '))
        saldo,extrato = depositar(saldo,leitor,extrato)
        
    elif opcao=="S":
        leitor=float(input('Digite o valor que deseja sacar: '))
        saldo, extrato, LIMITE_SAQUES = sacar(
            leitor=leitor,
            saldo=saldo,
            extrato=extrato,
            LIMITE_SAQUES=LIMITE_SAQUES
        )

    elif opcao=="E":
        exibir_extrato(saldo, extrato=extrato)


    elif opcao=='Q':
        break

    elif opcao=='NU':
        criar_usuario(usuarios)

    elif opcao=='NC':
        numero_conta=len(contas)+1
        conta = criar_conta(AGENCIA,numero_conta,usuarios)

        if conta:
            contas.append(conta)
    
    elif opcao=='LC':
        listar_contas(contas)

    else:
        print('Opcão Invalida, digite uma opçao valida')



