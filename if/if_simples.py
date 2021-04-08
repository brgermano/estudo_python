nome = input("Digite o nome func: ")
salario = float(input("Digite o salario do func: "))

if salario < 0:
    salario = salario * -1
    print("O salario é negativo")

print("O salário do funcionario {} é {}".format(nome, salario))