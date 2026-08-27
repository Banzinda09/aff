# 26. Simule um login: peça usuario e senha. Acesso concedido apenas se
#     usuario == "admin" e senha == "admin123".

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "admin123":
    print("Acesso concedido")
else:
    print("Acesso negado")
