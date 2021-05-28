import sys

nome = "Bruno Wayne"
idade = 30
peso = 92.3
list = ["youngling", "padawan", "knight", "master"]
categorias = ("youngling", "padawan", "knight", "master")

print("a var nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print("a var idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print("a var peso é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))
print("a var list é do tipo {} e tem {} bytes".format(type(list), sys.getsizeof(list)))
print("a var categorias é do tipo {} e tem {} bytes".format(type(list), sys.getsizeof(categorias)))