# Loops de repetição são formas de repetir um grupo de código sem precisar reescrever ele novamente podendo executar esse grupo uma quantidade predeterminada de vezes ou indeterminada vezes. Em Pyhton existem dois tipos métodos de repetição o 'For' e o 'While'.

# o For é uma estrutura que atua como um interador em Python, é um objeto que percorre uma lista de itens que estão em sequência e retorna os dados desses itens de maneira sucessiva, um elemento de cada vez.

numeros = list(range(1,101)) #lista de números de 1 até 100

for n in numeros:
    print(n)

print("\n")

for n in numeros:
    # pega a lista de números de 1 até 100 e imprima somente os números pares
    if(n % 2 == 0): # % módulo, resto da divisão entre os valores passados
        print(n,"é par")
    pass

print("\n")

for letra in "Ctrl+Play":
    print(letra)


print("\n")
# O While em python é uma das formas mais gerais de executar iterações em loops, pois diferente do for ele não está preso a uma lista, mas sim vai repetir até que a condição de parada passada para ele seja atingida.

'''
Estrutura:

while condição de parada:
    código que vai se repetir
'''

soma = 0 # o resultado da soma
numeros = range(1,1000) # lista de números de 1 a 999
i=0 # variável que vai controlar o index da lista de números


while soma < 100: #enquanto o valor de soma for menor que 200
    soma += numeros[i] #adicionar o valor atual na lista com base na posição passado por i
    print(f"O valor da soma agora é {soma} e o valor de somado foi {numeros[i]}") # mostar o valor da soma no loops atual
    i += 1 # aumentar o valor de i em 1 para ir para o próximo item da lista no loop seguinte
else: #O comando else é opcional e serve para execuar uma tarefa após o loop terminar ou caso não entre nele
    print("O valor de Soma agora é maior que 200, por isso não vou somar")