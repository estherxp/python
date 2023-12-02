# Desafio:
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta
def verf_parentes(expressao):
    parenteses = []

    for verifica in expressao:
        if verifica == '(':
            parenteses.append('(')
        elif verifica == ')':
            if not parenteses:
                return False
            parenteses.pop()

    return not parenteses

usuario = input('Digite uma expressão com parênteses: ')
if verf_parentes(usuario):
    print('Os parênteses estão corretos!')
else:
    print('Os parênteses não estão corretos!')

# quando encontra um parentese aberto, ele joga para a pilha ate encontrar um parentese fechado,
# "apagando" o ultimo elemento quando o looop terminar e a pilha estiver vazia significa que esta
# correto o codigo devera retornar true.
