#----------------------------------------------------------------------------------------------------
#*********************************************** DEPOSITAR ******************************************
#----------------------------------------------------------------------------------------------------

def depositar(saldo, valor, extrato, /):
# A '/' no final determina que todo argumentao passado será posicional    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f'Depósito realizado com sucesso ! Seu depósito é de R$ {valor:.2f} ')

    else:
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato
#----------------------------------------------------------------------------------------------------
#*********************************************** SACAR **********************************************
#----------------------------------------------------------------------------------------------------
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): 
# o '*' determina que todo valor passado depois dele é por key args ou seja chave valor     
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f'Saque Realizado com Sucesso !!!')
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

#---------------------------------------------------------------------------------------------------
#***************************************** EXTRATO *************************************************
#---------------------------------------------------------------------------------------------------
def exibir_extrato(saldo, /, *,  extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

#------------------------------------------------------------------
#**************************************** CRIAR USUARIO ***********
#------------------------------------------------------------------
    
def criar_usuario(usuarios): 
    cpf = input('Informe o CPF(Somente numeros): ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario: 
        print('\ Já existe usuário com este CPF')
        return
    
    nome= input('Informe o nome completo:')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o Endereço (Logradouro, nor - bairro - cidade/sigla estado):')
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereco})
    print('Usuario criado com sucesso !')
    
#-----------------------------------------------------------------
# ***************************************FILTRAR USUARIO *********   
#-----------------------------------------------------------------

def filtrar_usuario(cpf, usuarios):
        
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#-------------------------------------------------------------------    
#***************************************** CRIAR CONTA *************
#-------------------------------------------------------------------
   
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o  CPF: ')
    usuario = filtrar_usuario(cpf, usuario)
    
    if usuario: 
        print('Conta criada com sucesso !!!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
     
    print('Usuario não encontrado, fluxo de criação de contas encerrado !!!')
    