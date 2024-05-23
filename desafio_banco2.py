menu = '''

    Seja bem vindo ao Josh Bank!

    Qual operação deseja realizar hoje ?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

'''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input(f'Informe o valor do depósito:  '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: +R${valor:.2f}\n"
            print(f'Valor depositado: R${valor}\n')
        else:
            print('Falha na operação! Valor inválido para depósito. ')
            
    elif opcao =='s':
            valor = float(input(f'Informe o valor do saque: '))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                 print('Operação falhou! Você não tem saldo suficiente.')
            elif excedeu_limite:
                 print('Operação falhou! Você excedeu o limite diário para saque!')
            elif excedeu_saque:
                 print('Operação falhou! Você excedeu o número máximo de saques diário!')
            elif valor > 0:
                 saldo-=valor
                 extrato += f'  Saque: -R${valor:.2f}'
                 numero_saques += 1
                 print(f'Valor sacado: R${valor}')
            else:
                 print('Operação falhou! O valor é inválido!') 
  
    elif opcao == 'e':
         exibir_extrato = f'''
    ============ EXTRATO ==============
    {extrato}
    ===================================
    Saldo: R${saldo}
'''
         print(exibir_extrato)
    elif opcao == 'q':
         break
    else:
         print('Operação inválida, por favor selecione novamente a operação desejada.')

