# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário,
# se por acaso a Carteira de trabalho for diferente de zero.
# O Dicionário receberá também o ano de contratação e o saláro.
# Calcule e apresente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime

pessoas = {}

for _ in range(2):  # Ler 2 pessoas
    nome = input('Nome: ')
    ano_nascimento = int(input('Ano de Nascimento: '))
    carteira_trabalho = int(input('Número da Carteira de Trabalho (0 se não tiver): '))

    if carteira_trabalho != 0:
        ano_contratacao = int(input('Ano de Contratação: '))
        salario = float(input('Salário: '))
        idade = datetime.now().year - ano_nascimento
        aposentadoria = ano_contratacao + 35 - ano_nascimento  # Aposentadoria após 35 anos de contribuição
        pessoas[nome] = {'idade': idade, 'aposentadoria': aposentadoria, 'salario': salario}

print('\nInformações: ')
for nome, info in pessoas.items():
    print(f'Nome: {nome}, Idade: {info['idade']}, Aposentadoria: {info['aposentadoria']} anos, Salário: {info['salario']}')
