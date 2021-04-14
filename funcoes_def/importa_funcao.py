# para importar todas as funcoes do arquivo calc basta usar: import calc
# abaixo é um exemplo de como importar somente a função somar

#from calc import * < assim importa tudo
from calc import somar, subtrair

teste = somar(10, 3)
teste2 = subtrair(10, 3)

print(teste)
print(teste2)