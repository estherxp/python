# Escreva um programa que converta real para o Franco Congolês
# Saída esperada:
# 10,00 reais, equivalem a 5052,00 Francos Congoleses

print('********** Convertor de Moeda - Franco Congolês **********\n'
      'ATENÇÂO: Cotação utilizada de 23/09/2023.\n'
      '1 real = 0,0020 francos congoleses\n')

Real = float(input('Digite um valor em real R$: '))
Valor_franco = 505.52

Conversao = Valor_franco * Real

print(f'\n{Real} Reais, equivalem a {Conversao:.2f} Francos Congoleses')