# Faça um programa com uma função maior e menor, que leia uma lista com 5 valores informados
# pelo usuário e retorne esses valores e a posição deles

def maior_menor(lista):
    maior_valor = max(lista)
    menor_valor = min(lista)
    posicao_max = lista.index(maior_valor)
    posica_min = lista.index(menor_valor)
    return (f'Valores: {lista} '
            f'\n Maior: {maior_valor} A sua posição é: {posicao_max} '
            f'\n Menor: {menor_valor} A sua posição é: {posica_min}')


try:

    valores = []
    for i in range(5):
        valor = int(input('Digite um valor: '))
        valores.append(valor)

    resultado = maior_menor(valores)
    print(resultado)

except ValueError:
    print('Só aceitamos números.')
