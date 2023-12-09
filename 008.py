# Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.
# Saída esperada:
# O salário de 6000 com o reajuste de 60% será de : 9600

print('********** Calculadora de bônus salarial 60% **********\n')

salario = float(input('Digite o valor do salário atual: '))

salario_ajustado = salario + (salario * 0.6)

print(f'O salário de {salario} com o reajuste de 60% será de : {salario_ajustado}\n')

print('Finalizando aplicação...')