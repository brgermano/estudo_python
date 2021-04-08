mensagem1 = "Digite a quantidade de votos para"
mensagem2 = "O dia escolhido foi:"

segunda = int(input("{} Segunda-feira: ".format(mensagem1)))
terca = int(input("{} Terça-feira: ".format(mensagem1)))
quarta = int(input("{} Quarta-feira: ".format(mensagem1)))
quinta = int(input("{} Quinta-feira: ".format(mensagem1)))
sexta = int(input("{} Sexta-feira: ".format(mensagem1)))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("{} Segunda-feira".format(mensagem2))
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("{} Terça-feira".format(mensagem2))
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("{} Quarta-feira".format(mensagem2))
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("{} Quinta-feira".format(mensagem2))
else:
    print("{} Sexta-feira".format(mensagem2))