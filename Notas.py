#O comando print retorna informações para o usuário
#print("Olá, meu nome é Hadassa Millena")
'''
idade = 18
print(f'Minha idade é {idade}')

#Escreva um programa que leia a idade do usuário e retorne sua idade
idade = input("Digite a sua idade: ")
print(f'Sua idade é {idade}')

#Modo antigo de formatar um print, versão python 2
print('Sua idade é ',idade)

N1 = int(input('Digite o primeiro número: '))
N2 = int(input('Digite o segundo número: '))

Soma = N1 + N2

print(f'A soma de N1 e N2 é {Soma}')

Nome = 'Hadassa'
Sobrenome = 'Millena'
Nome_completo = Nome + ' ' + Sobrenome
print(Nome_completo)
'''
'''
#Declaração de variável
Nome = input('Digite seu nome: ')

Nome = Nome.strip() #Remove os espaços a direita e esquerda
print(f'A primeira letrata é: {Nome[0]}') Analiso a primeira letra da STRING

print(f'O tamanho do seu nome é {len(Nome)}') #A Função len(), retorna o tamanho da STRING

Nome = Nome.split() #Separa nossa STRING em lista
print(f'O Primeiro nome é: {Nome[0]}') #Analisando o Primeiro Nome
''''''
Nome = ['hadassa', 'millena', 'silva', 'dos', 'Santos']
Nome = '/'.join(Nome) #O método .join junta elementos da minha STRING
print(Nome)

Nome = input('Digite o seu nome: ')
Nome = Nome.upper() #Transforma toda minha STRING em Maiusculo
print(Nome)
Nome = Nome.lower() #Transforma toda minha STRING em Minusculo
print(Nome)'''
'''
altura = float(input('Digite sua altura: '))
if altura > 1.5: #Comparação de variável
    print('Você pode andar no brinquedo!')
else:   # Saída negativa
    print('Quem sabe no ano próximo ano!')
    
#--------------------------------------------
if altura > 1.5 and altura < 2:
    print('Você pode andar no Brinquedo.')
elif altura > 2:
    print('Você irá bater a cabeça! Está proibido!')
else:
    print('Você é muito pequeno, quem sabe no próximo ano.')
'''

'''
# listas
# Mutáveis
# Representadas por []
carro = ['Ferrari', 'Vermelha', '2023']

print(carro[1]) # ira retornar somente o que esta na posição inserida

carro.remove('Vermelha') # remove o valor 'vermelha'
print(carro) # irá retornar todo o conteúdo que está na lista

carro[1] = 'Amarelo'   # substitui o que estava na posição 1, no caso 'vermelho'
print(carro)

carro.append('Gasolina')     # cria no final da lista
print(carro)

carro.insert(1, '797 cv ')   # insere na posição 1
print(carro)

carro.pop(1) # remove o item na posição 1
print(carro)

len(carro)
print(carro) # retorna o tamanho da lista

idades = [4,5,6,2,33,44]
print(min(idades))
print(max(idades))
print(sum(idades))
'''
'''
# para deixar o programa mais bonito, ele ja mostra o numero que vc inseriu abaixo 
while ((numero:= input('Digite um número: ')) != 'sair'):
    print(str(numero))
'''
'''
lista = [numero for numero in iter(lambda : input('Digite um número: '), 'sair')]
# jeito melhor formatado de fazer o codigo (apenas para a estetica)

Aluno = list()           # Lista principal
dados = list()           # Lista secundária


for c in range(0, 3):
   dados.append(str(input('Nome: ')))  # Coleta de dados LS
   dados.append(int(input('Idade: ')))
   Aluno.append(dados[:]) # Inserção da cópia na LP
   dados.clear()

print(Aluno)
'''
'''
# listas
# Mutáveis
# Representadas por []
carro = ['Ferrari', 'Vermelha', '2023']

print(carro[1]) # ira retornar somente o que esta na posição inserida

carro.remove('Vermelha') # remove o valor 'vermelha'
print(carro) # irá retornar todo o conteúdo que está na lista

carro[1] = 'Amarelo'   # substitui o que estava na posição 1, no caso 'vermelho'
print(carro)

carro.append('Gasolina')     # cria no final da lista
print(carro)

carro.insert(1, '797 cv ')   # insere na posição 1
print(carro)

carro.pop(1) # remove o item na posição 1
print(carro)

len(carro)
print(carro) # retorna o tamanho da lista

idades = [4,5,6,2,33,44]
print(min(idades))
print(max(idades))
print(sum(idades))
'''
'''
# para deixar o programa mais bonito, ele ja mostra o numero que vc inseriu abaixo 
while ((numero:= input('Digite um número: ')) != 'sair'):
    print(str(numero))
'''
'''
lista = [numero for numero in iter(lambda : input('Digite um número: '), 'sair')]
# jeito melhor formatado de fazer o codigo (apenas para a estetica)
'''
Aluno = list()           # Lista principal
dados = list()           # Lista secundária


for c in range(0, 3):
   dados.append(str(input('Nome: ')))  # Coleta de dados LS
   dados.append(int(input('Idade: ')))
   Aluno.append(dados[:]) # Inserção da cópia na LP
   dados.clear()

print(Aluno)
'''
