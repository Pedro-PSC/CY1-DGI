#region Tuplas

print("Tuplas\n")

# As Tuplas são listas que possuem uma característica específica que a difere de uma lista comum, essa característica é o de que elas são imutáveis, ou seja, uma lista que após ser criada ela não pode ser modificada.

#Para criar uma tupla segue o mesmo conceite de criar uma lista, porém ao invés de usar o simbolo de '[]' na criação é usado o '()'.

t = ('um',2,'três',True,4.5,'cinco',False,'um')

#Para trabalhar com a tupla, por exemplo exibi-la em um print usa o simbolo do '[]'

print(t[2])
print(t[2:5])

#Nas tuplas assim como nas listas as funções de ver tamanho, localizar repetições e posição de um item também funcionam

print(len(t))
print(t.index(True))
print(t.count("um"))

#endregion

#region Conjuntos sets

print("\nConjuntos Sets\n")

#Conjuntos sets são Listas mutáveis (Podem ser alteradas) que possui como característica principal a não repetição de itens, ou seja, não pode ter dois ou mais itens com o mesmo valor. Ex.: (1,4,8,5,6,2,3,5,1,4,4,9) os números 1,4,5 repetem. o set de forma correta ficaria da seguinte forma (1,4,8,5,6,2,9)

#Para criar um conjunto set basta criar uma variáveil e após o sinal de '=' escrever 'set()'

x = set()

#Para adicionar elementos ao conjunto basta usar o método add() e como parãmentro passar o elemento que deseja inserir

x.add(1)
x.add(2)

print(x)

x.add(3)
x.add(1)
x.update([4,5,6])
print(x)

#No conjunto set todas as operações de listas, adicionar, apagar, organizar etc. Também funcionam com o conjunto.

#endregion

#region Boolean

print("\nBooleanas\n")

#Boolean são informações que só podem ter dois valores possíveis True ou False (Verdadeiro ou Falso)

a = True
podePular = False

c = 1 < 2 #True
d = 7 >= 10 #False

c = None #valor nulo, até preencher com algum valor podendo ser int, float, string, bool

print(a,podePular,c,d)

#endregion

#region Dicionários

print("\nDicionários\n")

# Um dicionário é uma estrutura de dados que armazena pares de chave-valor. Ele permite acesso rápido aos valores a partir de suas respectivas chaves.

# Criando um dicionário simples, use o simbolo de {} após declarar a variável. Um dicionário é uma coleção de pares chave-valor.

meu_dicionario = {
    "nome": ["João","Pedro"],  # "nome" é a chave, "João" é o valor
    "idade": [25],     # "idade" é a chave, 25 é o valor
    "cidade": ["Belo Horizonte"],  # "cidade" é a chave, "Belo Horizonte" é o valor
}

# Acessando valores em um dicionário
# Para acessar um valor, use a chave correspondente:
print(meu_dicionario["nome"])  # Saída: João, Pedro

# Para adicionar acrescentar um valor novo a uma chave
meu_dicionario["idade"].append("27")
meu_dicionario["cidade"].append("Lagoa Santa")

print(meu_dicionario) 

# Adicionando uma nova chave-valor ao dicionário
meu_dicionario["profissao"] = ["Engenheiro","Professor"]
print(meu_dicionario)  # Agora inclui "profissao": "Engenheiro"

# Modificando o valor de uma chave existente
meu_dicionario["idade"] = 26  # Atualizamos a idade para 26
print(meu_dicionario["idade"])  # Saída: 26

# Removendo uma chave-valor do dicionário
del meu_dicionario["cidade"]  # Remove a chave "cidade" e seu valor
print(meu_dicionario)

# Iterando sobre um dicionário
# Podemos percorrer todas as chaves ou valores do dicionário:
for chave in meu_dicionario:
    print(f"Chave: {chave,}, Valor: {meu_dicionario[chave]}")

# Usando os métodos .keys(), .values(), e .items()
print(meu_dicionario.keys())   # Retorna todas as chaves do dicionário
print(meu_dicionario.values()) # Retorna todos os valores do dicionário
print(meu_dicionario.items())  # Retorna todos os pares chave-valor como tuplas

# Verificando se uma chave existe no dicionário
if "nome" in meu_dicionario:
    print("A chave 'nome' está presente no dicionário!")

# Limpando o dicionário
meu_dicionario.clear()  # Remove todos os itens do dicionário
print(meu_dicionario)  # Saída: {}

#endregion