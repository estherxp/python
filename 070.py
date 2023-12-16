# Escreva um programa que crie um dicionário com os nomes e preços de 5 produtos.
# Em seguida, exiba o produto mais barato e o mais caro.


produtos = {
    'Coca-Cola': 10.0,
    'Dolly': 4.0,
    'Fanta': 7.0,
    'Pepsi': 9.0,
    'Guaraná': 6.0
}

produto_mais_barato = min(produtos, key=produtos.get)
produto_mais_caro = max(produtos, key=produtos.get)

print("Produto mais barato:", produto_mais_barato, "- Preço:", produtos[produto_mais_barato])
print("Produto mais caro:", produto_mais_caro, "- Preço:", produtos[produto_mais_caro])
