# EXERCICIO 22

'''
escreva um programa que le dois numeros;
depois imprima o maior deles
'''

numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))

print(numero_1)
print(numero_2)

if numero_1 > numero_2:
    print(numero_1)

if numero_2 > numero_1:
    print(numero_2)

if numero_2 == numero_1:
    print('Números iguais.')