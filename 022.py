#Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média,
#é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).

def media_notas(a,b,c,d,e):
        if (a+b+c+d+e) / 5 < 6:
            print(f'\nA média das notas é insuficiente.\nA média é {(a+b+c+d+e) / 5}.')
        elif (a+b+c+d+e) / 5 >= 6 and (a+b+c+d+e) / 5  <= 7:
            print(f'\nA média das notas é suficiente.\nA média é {(a+b+c+d+e) / 5}.')
        elif (a+b+c+d+e) / 5 >= 7 and (a+b+c+d+e) / 5 <= 9:
            print(f'\nA média das notas é bom\nA média é {(a+b+c+d+e) / 5}.')
        elif (a+b+c+d+e) / 5 >= 9:
            print(f'\nA média das notas é excelente\nA média é {(a+b+c+d+e) / 5}.')

def check_nota(a):
    while True:
        if a >= 0 and a <= 10:
            print(f'Nota {a} confirmada.')
            break
        else:
            a = float(input('Valor inválido. Por favor, digite uma nota entre 0 e 10: '))

while True:
    try:
        n1 = float(input('Digite a nota 1: '))
        check_nota(n1)
        n2 = float(input('Digite a nota 2: '))
        check_nota(n2)
        n3 = float(input('Digite a nota 3: '))
        check_nota(n3)
        n4 = float(input('Digite a nota 4: '))
        check_nota(n4)
        n5 = float(input('Digite a nota 5: '))
        check_nota(n5)

    except ValueError:
        print('Valor inválido')

media_notas(n1, n2, n3, n4, n5)
