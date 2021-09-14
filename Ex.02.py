usuario=input('Usuário: ')
senha=input('Senha: ')
while usuario == senha:
    print('Senha deve ser diferente do Usuário')
    usuario=input('Usuário: ')
    senha=input('Senha: ')
else:
    print('Cadastro feito com sucesso')
