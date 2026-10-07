# ESTRUTURA IF

'''
O IF VAI RECEBER UMA CONDIÇÃO, QUE SE FOR AVALIADA COMO VERDADEIRA
O SOFTWARE ENTRA EM UM BLOCO DE CODIGO DIFERENTE;
CASO A CONDIÇÃO NÃO SEJA VERDADEIRA, O BLOCO É IGNORADO.
A ESTRUTURA E SINTAXE É A SEGUINTE:

IF CONDIÇÃO:
    BLOCO A SER EXECUTADO
'''

if 10 > 5:
    verdura = 'cenoura'
    print('Entrou no if')
    print(verdura)

print('ANTES DO IF')

if 5 > 10:
    print('if falso')

print('DEPOIS DO IF')

nome = 'janier'
idade = 29

if nome == 'janier' and idade == 29:
    print('Olá, Janier!')

