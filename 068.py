# Escreva um programa que crie um dicionário com as informações de 5 países, como nome, capital,
# população e idioma oficial. Em seguida, permita que o usuário digite o nome de um país e exiba suas informações.

paises = {
    'Brasil': {'capital': 'Brasília', 'populacao': 213993437, 'idioma': 'Português'},
    'EUA': {'capital': 'Washington, D.C.', 'populacao': 332915073, 'idioma': 'Inglês'},
    'China': {'capital': 'Pequim', 'populacao': 1444216107, 'idioma': 'Chinês'},
    'Índia': {'capital': 'Nova Delhi', 'populacao': 1393409038, 'idioma': 'Hindi'},
    'Rússia': {'capital': 'Moscou', 'populacao': 145912025, 'idioma': 'Russo'}
}

pais_desejado = input("Digite o nome de um país: ")

if pais_desejado in paises:
    informacoes = paises[pais_desejado]
    print(f"Informações sobre {pais_desejado}: {informacoes}")
else:
    print(f"País {pais_desejado} não encontrado.")
