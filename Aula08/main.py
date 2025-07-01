# Para importar um módulo/biblioteca basta usar o comando import e em seguida colocar o nome do módulo ou biblioteca. OBS.: as importações elas tem que ser sempre a primeira coisa que você faz no programa
import math
import matematica.calculadora as c #importar todo o modulo e colocar um apelido
from matematica.calculadora import Soma, Multiplicacao #impotar só as funções desejadas do módulo


# use o o comando 'dir()' para visualizar todas as funções existentes neste módulo ou biblioteca

print(dir(math))

# para saber como uma função de um módulo ou biblioteca funciona basta usar o comando 'help()' passando o nome da função que deseja saber o funcionamento

print(help(math.sqrt))

numero = math.sqrt(144)
print(numero)

print('\n\n')

print(c.Soma(10,30))
print(c.Subtracao(30,10))
print(c.Multiplicacao(30,10))
print(c.Divisao(30,10))

print(dir(c))
print(help(c.Soma))

print(Soma(40,60))
print(Multiplicacao(40,60))