#Escreva um programa que peça ao usuário um número de 1 a 7 e
# imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).

dias_semana = ['Domingo','Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado']

numero = int(input('Digite um número entre [0] e [6]: '))

print(f'\nO dia da semana correspondente a {numero} é {dias_semana[numero]}')