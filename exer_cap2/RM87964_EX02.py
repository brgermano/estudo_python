assinatura_cliente = int(input("Escolha sua assinatura \n 1 - Basic / 2 - Silver / 3 - Gold / 4 - Platinum: "))
faturamento_anual = float(input("Digite o seu faturamento anual: "))

mensagem = "O valor do bônus é:"

calculo_basic = 30 / 100 * faturamento_anual
calculo_silver = 20 / 100 * faturamento_anual
calculo_gold = 10 / 100 * faturamento_anual
calculo_platinum = 5 / 100 * faturamento_anual

if assinatura_cliente==1:
    print("{} {}".format(mensagem, calculo_basic))
elif assinatura_cliente==2:
    print("{} {}".format(mensagem, calculo_silver))
elif assinatura_cliente==3:
    print("{} {}".format(mensagem, calculo_gold))
elif assinatura_cliente==4:
    print("{} {}".format(mensagem, calculo_platinum))