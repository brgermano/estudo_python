personagens=[]
categorias=[]

for x in range(10):
    personagens.append(input("Informe o nome do personagem: "))
    categorias.append(input("Informe a categoria do personagem: "))

for indice in range(10):
    print("O personagem {} é um (a) {}".format(personagens[indice], categorias[indice]))
