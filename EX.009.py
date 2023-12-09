#Simulador de Caixa Eletrônico
# - Simule um caixa eletrônico. Primeiro pergunte ao usuário qual valor ele quer retirar,
# depois dê o dinheiro com o menor número possível de notas.
print('----Bem-vindo ao caixa eletrônico----')
valor = int(input('Digite o valor para o saque: '))
notas_disponiveis = [200,100,50,20,10,5]
notas_entregues = {}

for nota in notas_disponiveis:
    if valor >= nota:
        quantidade = valor // nota #Divisão de int, resulta int, ou de float por int ou float só parte inteira
        valor %= nota   #x %= y equivale a x = x%y
        notas_entregues[nota] = quantidade
print("Você receberá as seguintes notas:")
for nota, quantidade in notas_entregues.items():
    print(f"{quantidade} notas de {nota} reais")

#operador usado para dividir, resulta int ou de float mas somente a parte inteira.
#aprendi no site FOLHA DE CONSULTA - PYTHON