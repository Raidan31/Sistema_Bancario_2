def banco_dan ():
    dicio = {}
    lista = dicio
    

    while True:
        entrada = int (input ( " 1 - Adicionar uma nova conta com saldo inicial; 2 - Fazer um depósito em uma conta existente; 3 -Fazer um saque de uma conta existent; 4 - Ver o saldo de uma conta existente; 5 - Sair do programa:  " ))
        
        if  entrada == 1:
            numero_conta = int(input("Informe o Nº da Conta: "))
            nome_cliente = input("Infome o nome do cliente: ")
            saldo_inicial = int(input("Informe o valor do deposito do saldo inicial: "))
            dicio[numero_conta] = {'saldo': saldo_inicial, 'cliente': nome_cliente}
            print (f"Foi depositado na conta do cliente: {nome_cliente}, número da conta: {numero_conta} o valor de R$ {saldo_inicial},00   ////////// Operação Encerrada /////////// Retornando ao menu inicial ///////////") 
        elif entrada == 2:

            selecionar_conta =  int(input("Informe o número da conta que deseja realizar o deposito: "))
            deposito_valor = int(input("Informe o valor que deseja depositar: "))
            dicio[selecionar_conta]['saldo'] += deposito_valor
            print(f"Foi depositado na conta do cliente: {dicio[selecionar_conta]['cliente']} número da conta {selecionar_conta}, o valor de {deposito_valor},00   ////////// Operação Encerrada /////////// Retornando ao menu inicial ///////////")

        elif entrada == 3:
            conta_saque =  int(input("Informe o número da conta que deseja realizar o saque: "))
            valor_saque = int(input("Informe o valor que deseja sacar: "))
            if valor_saque >  dicio.get(conta_saque):
                print("Saldo Insuficiente!")
            else:
                 dicio[conta_saque] = dicio.get(conta_saque) - valor_saque
                 saldo = dicio.get(conta_saque) 
                 print(f"A conta {conta_saque}, foi realizado o saque de {valor_saque},00, saldo atual {saldo}  ////////// Operação Encerrada /////////// Retornando ao menu inicial ///////////")
        
        elif entrada == 4:
            conta_saldo = int(input("Informe o número da conta que deseja verificar o saldo: "))
            saldo_conta = dicio.get(conta_saldo)
            print (f"O saldo da conta {conta_saldo} é de R$ {saldo_conta},00 ")
        
        elif entrada == 5:
            print("Obrigado por ser nosso cliente! Volte Sempre!!")  
            break
        
        else:
            print("Valor inválido, selecione um outro número!") 
            

banco_dan ()

