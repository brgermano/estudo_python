peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = float(peso / (altura * altura))
mensagem = "Sua faixa de imc é:"

if imc < 16.00:
    print("{} Baixo peso Grau III".format(mensagem))
elif imc >= 16.00 and imc < 16.99:
    print("{} Baixo peso Grau II".format(mensagem))
elif imc >= 17.00 and imc < 18.49:
    print("{} Baixo peso Grau I".format(mensagem))
elif imc >= 18.50 and imc < 24.99:
    print("{} Peso ideal".format(mensagem))
elif imc >= 25.00 and imc < 29.99:
    print("{} Sobrepeso".format(mensagem))
elif imc >= 30.00 and imc < 34.99:
    print("{} Obesidade Grau I".format(mensagem))
elif imc >= 35.00 and imc < 39.99:
    print("{} Obesidade Grau II".format(mensagem))
else:
    print("{} Obesidade Grau III".format(mensagem))
