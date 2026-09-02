# Funções para as operações matemáticas
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida!"
    return a / b

# Função principal que gerencia o fluxo
def calculadora():
    print("=== CALCULADORA ===")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
            elif opcao == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif opcao == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcao == '4':
                print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.")
    else:
        print("Opção inválida!")

# Executa a calculadora
calculadora()