#Calculadora de Juros Compostos
# - Solicite ao usuário o principal, a taxa de juros anual e o número de anos,
# e imprima o valor do investimento após esse número de anos

print('----Calculadora de Juros Compostos----')
taxa_juros_anul = float(input('Digite a taxa de juros anual (em decimal): '))
qnt_anos = int(input('Digite a quantidade de anos: '))
valor_inicial = float(input('Digite o valor do investimento inicial ou deixe em branco para zero: ')or 0)
valor_final = valor_inicial * (1 + taxa_juros_anul) ** qnt_anos

print(f'Depois de {qnt_anos} anos da aplicação, você iria receber ${valor_final} de juros compostos')

