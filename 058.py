# Crie um programa onde serão informados diversos valores em uma lista.
# Caso o número já exista ele não será adicionado.
# No final, serão exibidos todos os valores únicos em ordem crescente
try:
    valores = []
    while True:
        valor = input('Digite um valor (ou "fim" para sair): ').lower().upper()
        if valor.lower() == 'fim':
            break
        valor = int(valor)
        if valor not in valores:
            valores.append(valor)

    valores_unicos = sorted(valores)
    print(f'Valores unicos em ordem crescente: {valores_unicos}')

except ValueError:
    print('Só aceitamos números!')