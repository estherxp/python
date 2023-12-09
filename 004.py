# Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
# V = (4/3) . π . r³
# A = 4 . π . r²
# Saída esperada:
# Volume da Esfera: Y
# Área da esfera: X

import math

print('********** Calculadora de volume e área de uma esfera **********\n')

R = float(input('Digite o raio de uma espera: '))
V = (4/3) * math.pi * (R**3)
A = 4 * math.pi * (R**2)

print(f'\nVolume da Esfera: {V:.2f}'
      f'\nÁrea da esfera: {A:.2f}')

print('\nFinalizando aplicação...')