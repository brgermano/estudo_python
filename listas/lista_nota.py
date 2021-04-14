notas = []

opcao = -1
while opcao != 3:
    print("1 - informar nota \n 2 - exibir notas \n 3 - calcular media \n 4 - sair")
    opcao = int(input("Escolha sua opção: "))
    if opcao == 1:
        notas.append(float(input("Digite a nota: ")))
    elif opcao == 2:
        for x in notas:
            print(x)
    elif opcao == 3:
        print(sum(notas)/len(notas))