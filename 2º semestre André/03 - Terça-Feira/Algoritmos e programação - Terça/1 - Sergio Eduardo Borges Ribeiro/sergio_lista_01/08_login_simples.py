# 8. Receba a senha digitada pelo usuário e compare com a senha correta "1234".
#    Exiba "Acesso Permitido" ou "Acesso Negado".

SENHA_CORRETA = "1234"
senha = input("Digite a senha: ")

if senha == SENHA_CORRETA:
    print("Acesso Permitido")
else:
    print("Acesso Negado")
