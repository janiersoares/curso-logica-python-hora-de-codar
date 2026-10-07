# EXERCICIO 21

'''
CRIE UM PROGRAMA QUE RECEBE O NUMERO DE RODAS QUE O VEICULO POSSUI;
SE FOR MAIS QUE 2, IMPRIMA UMA MENSAGEM PARA PAGAR PEDAGIO;
SE FOR IGUAL A 2, IMPRIMA UMA MENSAGEM DIZENDO QUE PODE PASSAR LIVREMENTE;
'''

rodas = int(input('Quantas todas tem o seu veiculo? '))

if rodas > 2:
    print('Necessário pagar pedágio!')

else:
    print('Passagem livre!')