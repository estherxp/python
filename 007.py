# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
# Saída esperada:
# A dobro de 9 é : 18
# A triplo de 9 é : 27
# A raiz quadrada de 9 é : 3

print('********** Calculadora de dobro-triplo e raiz quadrada **********\n')

n1 = float(input('Digite um número inteiro: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** 0.5

print(f'A dobro de {n1} é : {dobro}'
      f'\nA triplo de {n1} é : {triplo}'
      f'\nA raiz quadrada de {n1} é : {raiz:.2f}')

print('\nFinalizando aplicação...')

