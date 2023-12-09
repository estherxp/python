#Escreva um programa que peça ao usuário uma senha e verifique se ela está correta
# (a senha correta é "python123").

def acesso(a):
    if a == 'python123':
        print('\nAcesso liberado.')
    else:
        print('\nSenha incorreta.\nAplicação finalizada.')

user = input('Login: ')
password = input('Password: ')

acesso(password)


