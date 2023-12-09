#Crie um programa que verifica se uma pessoa pode ser doadora de sangue,
#considerando a idade e os critérios de saúde.

idade = int(input('Digite a sua idade: '))

if idade >= 16 and idade<= 69:
        peso = float(input('Digite seu peso: '))

        if peso > 50:
            dormiu = float(input('Quantas horas você dormiu? '))

            if dormiu >= 8:
                print('Você pode doar')

            else:
                print('Você dormiu muito pouco.')
        else:
            print('Você não tem o peso adequado')
else:
    print('Não pode doar! Erro idade.')