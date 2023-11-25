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
