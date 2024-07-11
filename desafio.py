menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")

        else:
            print("Valor inválido, o depósito precisa ser maior que zero.")


    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))


        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque_diario = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")

        if excedeu_limite:
            print("O valor do saque excede o limite permitido!")

        if excedeu_saque_diario:
            print("Número máximo de saques atingido!")    

        elif valor > 0:
            if valor <= limite:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"    
                numero_saques += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso!")

            else:
                print(f"O valor do saque não pode exceder R${limite:.2f}!")

        else:
            print("Valor inválido, o saque deve ser maior que zero.")    


    elif opcao == 'e':
        print("\n" + "#" * 35)
        print("EXTRATO".center(35))
        print("#"* 35)
        if not extrato:
            print("Não foram realizadas movimentações nessa conta.".center(35))
        
        else:
            for linha in extrato.split('\n'):
                if linha:
                    print(linha.center(35))


        print("#" * 35)
        print(f"Saldo: R${saldo:.2f}".center(35))
        print("#" * 35)


    elif opcao == 'q':
        break  

    else:     
        print('Operação inválida, por favor selecione novamente a operação desejada.')
