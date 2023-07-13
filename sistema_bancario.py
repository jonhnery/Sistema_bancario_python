saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("""   MENU    
          [1] Depositar
          [2] Sacar
          [3] Extrato
          [0] Sair     
          """)
    opcao = int(input("Digite sua opção: "))

    if opcao == 1: #depositar#
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido")
        
    
    elif opcao == 2: #sacar#
        valor = float(input("Valor de saque: "))

        if valor > saldo:
            print("Saldo insuficiente")

        elif valor > limite:
            print("Valor de saque excede o limite por operação")

        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saque diário excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido")

        
    elif opcao == 3: #extrato#

        print("\n########## EXTRATO ##########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#".center(40,"#"))

    elif opcao == 0: #sair#
        break
    else:
        print("Opção Inválida")

        




