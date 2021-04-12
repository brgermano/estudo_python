valorUsuario = int(input("Digite um valor numérico inteiro: "))

primeiroValor = 0
segundoValor = 1
iteracao = 0


if valorUsuario <= 0:
    print("Digite um numero maior que zero")
else:
    print("Esse fibo tem {} elementos".format(valorUsuario), ":")
    while iteracao < valorUsuario:
        print(primeiroValor, end=', ')
        n = primeiroValor + segundoValor
        primeiroValor = segundoValor
        segundoValor = n
        iteracao += 1