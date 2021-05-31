#criando um dicionario com dados
dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}

print("O objeto dicionario é do tipo {}".format(type(dicionario)))

#print(dicionario["R2-D2"])

#mostrando todos valores (categorias)
#for valor in dicionario.values():
#    print(valor)

#mostrando todas as chaves (personagens)
#for chave in dicionario.keys():
#    print(chave)

# mostrando chaves e valores
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

    