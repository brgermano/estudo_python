pontuacao = int(input("Informe a pontuação: "))

if pontuacao > 1000:
    print("Voce ganhou 3gb de bonus")
elif pontuacao > 500:
    print("Vc ganhou 1,5gb")
elif pontuacao > 200:
    print("vc ganhou 500mb")
else:
    print("vc n ganho nada")
#>1000 3gb
#>500 1,5gb
#>200 500mb
#<200 nada