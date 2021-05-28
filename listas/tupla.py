categorias = ("youngling", "padawan", "knight", "master")

print(categorias)

print(categorias[0]) # youngling
print(categorias[1]) # padawan

#usando um indice negativo para exibir o ultimo item da tupla
print(categorias[-1]) # master

# Exibindo cada item da tupla usando um loop

print("======= LOOP ========")
for categoria in categorias:
    print(categoria)