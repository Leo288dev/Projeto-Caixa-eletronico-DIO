deposito = 0
saque = 0
saldoDep = []
saldoSaq = []
extrato = 0
cont = 0

#BLOCO MENU INICIAL --------------------------------------------------------------------------

nome = ' Banco DIO '
print('=-' * 18)
print(nome.center(35, '$'))
print('=-' * 18)
while True:
    menu = '''
                [A] DEPÓSTIO
                [B] SAQUE
                [C] EXTRATO
                [D] ENCERRAR
    '''
    print(menu)
    menu = input('Digite a opção desejada: ').upper()

#--------------------------------------------------- BL DEPÓSITO ------------------------------------------------------
    if menu in 'A':
        if menu == 'A':
            print('')
            print('-------- OPÇÃO DEPÓSITO --------')
            print('')
            print('INSIRA O VALOR PARA DEPÓSITO ...')
            dep = int(input('Valor à depositar: '))
            print('')
            if dep <= 0:
                print('*' * 50)
                print('Depósitos APENAS com VALORES POSITIVOS')
                print('')
                print('Retornando para o menu principal...\n'
                      '[A] DEPÓSTIO, [B] SAQUE, [C] EXTRATO, [D] ENCERRAR)')
                print('')
                print('*' * 50)
            else:
                deposito += dep
                print('=-' * 36)
                print(f'DEPÓSITO REALIZADO COM SUCESSO R$ {deposito}')
                print('=-' * 36)
                saldoDep.append(dep) #--------------------------------------------------------------------------------- lista com historico de depositos
                print(F'SALDO ATUAL R$ {deposito}')
#-----------------------------------------------------------------------------------------------------------------------
#---------------------------------------------BL SAQUE -----------------------------------------------------------------
    elif menu in 'B':
        print('')
        print('-------- OPÇÃO SAQUE --------')
        print('')
        print('INSIRA O VALOR PARA SAQUE ...')
        print(F'Saldo atual R$ {deposito}')
        saq = int(input('Digite o valor à sacar R$ '))
        if saq != 0:
            if saq <= deposito:
                cont += 1
                if cont <= 3:
                    print('')
                    print(f'Saque de R$ {saq} efeutado com sucesso !!! ')
                    deposito -= saq
                    print(f'Saldo atual R$ {deposito}')
                    saldoSaq.append(saq) #----------------------------------------------------------------------------------------Lista com histórico de saques
                else:
                    print('Numero de operções SAQUE excedido !!!')
            else:
                print('Operação negada Saque superior ao Saldo !!!')
                print(F'SALDO ATUAL R$ {deposito}')
                print('-' * 36)
        else:
            print('=' * 36)
            print('VALOR INVÁLIDO PARA SAQUE')
            print('=' * 36)
            print('')
#-----------------------------------------------------------------------------------------------------------------------
#---------------------------------------------- BL EXTRATO --------------------------------------------------------------

    elif menu == 'C':
        if len(saldoDep) == 0 and len(saldoSaq) == 0:
            print('')
            print('--------------- OPÇÃO EXTRATO ---------------')
            print('=' * 45)
            print('Não há historico de transações até o momento')
            print('=' * 45)

        else:
            print('')
            print('------------------ OPÇÃO EXTRATO -------------------')
            print('')
            print(f'Operações depósito realizadas .................{saldoDep}')
            print(f'Operações Saque realizadas ....................{saldoSaq}')
            print('')
            print('-' * 52)
            print(F'SALDO ATUAL R$ {deposito}')


#-----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------BL ENCERRAMENTO -----------------------------------------------------------
    elif menu == 'D':
        print('')
        print('=-' * 18)
        print(nome.center(35, '$'))
        print('=-' * 18)
        print('')
        print('Obrigado pode escolher nossos serviços')
        print('')
        print('Digital Inovatio one Financial o seu banco !!!')
        print('*** FIM ***')
        break

#-----------------------------------------------------------------------------------------------------------------------
#-------------------------------------------BL MENU PRINCIPAL  SENÃO ---------------------------------------------------

    else:
        print('=-' * 36)
        print('')
        print('Favor escolher entre: '
              '[A] DEPÓSTIO, [B] SAQUE, [C] EXTRATO, [D] ENCERRAR ')
        print('')
        print('=-' * 36)


