''' TASK 1 - modularizar as funções existentes como: 
[ok] sacar, 
[ok] depositar, 
[ok] visualizar histórico,
 
TASK 2 - criar 2 funções novas 
[] criar usuario(cliente do banco) e 
[] conta corrente (vincular com usuario)
'''
import menu_servicos



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'
usuarios = []
contas = []

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuario
[nc] Nova Conta
[q] Sair

=> """



while True:

    opcao = input(menu)
#----------------------------- DEPOSITO ---------------------------    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = menu_servicos.depositar(saldo, valor, extrato)

#-----------------------------SAQUE---------------------------------
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = menu_servicos.sacar(
            saldo=saldo, 
            valor=valor, 
            extrato=extrato, 
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES)
#----------------------------EXTRATO-------------------------------    
    elif opcao == "e":
        menu_servicos.exibir_extrato(saldo, extrato=extrato)
        
#---------------------------NOVO USUARIO -----------------------
    elif opcao == 'nu': 
        menu_servicos.criar_usuario(usuarios)
#------------------------------- Nova Conta ----------------------------------
    elif opcao == 'nc': 
        numero_conta = len(contas) + 1
        conta = menu_servicos.criar_conta(AGENCIA, numero_conta, usuarios)
        
        if conta: 
            contas.append(conta)
            
#----------------------------SAIR------------------------------------
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
   