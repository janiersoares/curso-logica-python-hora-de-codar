# EXERCICIO 23

'''
CRIE UM PROGRAMA COM A CARIAVEL SALARIO
SE FOR MAIOR QUE 1800 IMPRIMA UMA MENSAGEM DE QUE É 
NECESSÁRIO PAGAR IMPOSTO DE RENDA;
SE NÃO IMPRIMA UMA MENSAGEM QUE NÃO PRECISA PAGAR IR
'''

salario = float(input('Qual seu salario? '))

if salario >= 1800:
    print(f'Seu salário é de R${salario}, necessário pagar IR.')

else:
    print(f'Seu salário é de R${salario}, não precisa pagar IR.')