def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite 1, 2, 3 ou 4: ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o teste Nivaldo número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(num1, "+", num2, "=", soma(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtracao(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicacao(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divisao(num1, num2))

    else:
        print("Opção inválida")

# Chama a função calculadora
calculadora()
