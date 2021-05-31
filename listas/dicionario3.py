#criando um dicionario com dados
dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
#removendo o item cuja chave é R2-D2
dicionario.pop("R2-D2")

print("===============================")

#exibindo o dicionário completo após a remoção
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

#removendo ultimo item

print("=================================")

dicionario.popitem()

for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

print("====================== aqui")
#apagando tudo do dicionario
dicionario.clear()
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))