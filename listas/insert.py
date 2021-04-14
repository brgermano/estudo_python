#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor em uma posição específica da lista
jedi.insert(0, "OLOKO")

jedi.insert(5, "PESADO")

#remove o ultimo item
jedi.pop()

#remove segundo item
jedi.pop(1)

#remote item especifico
jedi.remove("Luke")
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)