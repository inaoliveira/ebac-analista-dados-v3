"""
Projeto: Calculadora de Operações Básicas
Curso: Analista de Dados v3 (EBAC)
Objetivo: Exercitar fundamentos de lógica, tipos de dados e entrada/saída de informações.
Autor: Inácio Oliveira
"""

# Solicitar número
number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))


# Solicitar Operação
operacao = input("Escolha a operação (+, -, *, /):")

# Verifiicar operação escolhida
if operacao == "+":
    resultado = number1 + number2
elif operacao == "-":
    resultado = number1 - number2
elif operacao == "*":
    resultado = number1 * number2
elif operacao == "/"    :
    if number2 != 0:
        print("Resultado:", number1 / number2)
    else:
        print("Não é possível dividir por zero.")

else:
    print("Operação inválida")

print("Resultado:", resultado)
