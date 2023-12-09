#Gerador de Histórias
#- Solicite ao usuário seu nome, sua cidade e seu animal de estimação, então use essas informações para gerar uma
# história curta.

print("---- Bem-vindo ao gerador de história ----")

print("Para gerar a sua história digite as informações abaixo:")
nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")
animal = input("Digite o nome do seu animal de estimação: ")

historia = (f"Uma vez, em {cidade}, havia uma pessoa chamada {nome} adorava passear com o seu companheiro {animal}."
            f" Eles tinham aventuras incríveis juntos e eram conhecidos por toda a cidade como uma dupla inseparável")

print(historia)