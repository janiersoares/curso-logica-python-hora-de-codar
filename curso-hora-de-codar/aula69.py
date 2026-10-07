# ESTRUTURA ELSE

'''
A ESTRUTURA ELSE VAI OCORRER APENAS QUANDO O IF NÃO FOR EXECUTADO;
OU SEJA, PODEMOS EXECUTAR OUTRA PARTE DO CODIGO PARA UMA SITUAÇÃO
INVERSA DO IF.

ESTRUTURA:

IF CONDIÇÃO:
    CODIGO

ELSE:
    CODIGO
'''

poupanca = 200

saque = 100

if saque <= poupanca:
    print(f'Você sacou R${saque}.')

else:
    print(f'Você não tem saldo para sacar {saque}.')