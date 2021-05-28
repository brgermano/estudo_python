restaurantes = ["Kibon", "Sukiya", "A Feijoada", "Makis", "Giraffas", "Viena"]
notas = [4.9, 4.6, 4.4, 4.7, 4.4, 4.4]
fretes = [6.99, 7.99, 9.90, 7.99, 5.99, 12.49]

restaurantesOrdenados = []

for restauranteAtual in restaurantes:
    indiceRestaurante = restaurantes.index(restauranteAtual)
    notaRestaurante = notas[indiceRestaurante]
    freteRestaurante = fretes[indiceRestaurante]

    #print("Restaurante: {} - Nota: {} - Frete: {}".format(restauranteAtual, notaRestaurante, freteRestaurante))
    for notaAtual in notas:
        if notaRestaurante > notaAtual:

