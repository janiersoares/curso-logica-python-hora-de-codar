# EXERCICIO 24

'''
ESCREVA UM PROGRMA QUE RECEBE DOIS NUMEROS;
INSIRA A MULTIPLICAÇÃO ENTRE ELES EM UMA VARIAVEL;
SE FOR MENOR OU IGUAL A 100 O RESULTADO INSIRA UMA MENSAGEM 
DE QUE O NUMERO É BAIXO;
SE NÃO O NUMERO É ALTO
'''

numero_1 = float(input('insira um numero: '))
numero_2 = float(input('insira um numero: '))

multiplicacao = numero_1 * numero_2

print(multiplicacao)

if multiplicacao <= 100:
    print(f'O numero {multiplicacao} é baixo.')

else:
    print(f'O numero {multiplicacao} é alto.')