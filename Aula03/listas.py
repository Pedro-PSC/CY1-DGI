#region Base sobre Listas
#Listas são formas da gente armazenar vários dados em um só local, como por exemplo uma lista de convidados para uma festa.
#Para criar uma lista a gente precisa dar um nome a ela (as mesmas regras para declarar variáveis se aplica à criação de listas) em seguida preencher dentro de '[]' os itens da sua lista ou deixar vazio para preencher ao decorrer do código.

convidados = ["Pedro","Isac","Guilherme","David","Marcos"]

print(convidados)


#Para exibir um item específico da sua lista basta na hora de chamar a lista usar o [] e inserir um valor de index dentro

print(convidados[3]) #David
print(convidados[:3]) #Pedro, Isac, Guilherme
print(convidados[-3]) #Guilherme

#endregion

#region Operações com Listas (Adição e Remoção)

#Diferente de uma string que é imutável a lista pode ser modificada, alterando algum de seus itens da seguinte forma
convidados[4] = "Henrrique"
print(convidados)

#Para acrescentar itens a sua lista pode usar a função append() e dentro do '()' inserir qual tipo de informação você quer na sua lista. O item adicionado sempre vai ser posicionado no final da sua lista
convidados.append("Marcos")
print(convidados)

#Outra forma de adicionar um item na lista porém em uma posição de index desajada é usando a função insert()
convidados.insert(2,"Heitor")
print(convidados)

#A primeira forma de remover um item da lista é simplesmente deletar ele da lista com o comando del
del convidados[0]
print(convidados)

#A segunda forma de remover um item da lista é remove-lo porém salvando em uma variável para backup exibir ou fazer alguma operação futura, para isso usamos a função pop(). Se a não for passando nenhum parãmetro dentro da função '()' ela removerá o último da lista e vai armaze-lo na variável.
convidadoRemovido = convidados.pop()
print(convidados)
print(convidadoRemovido,"foi banido da festa!")

convidadoRemovido = convidados.pop(1)
print(convidados)
print(convidadoRemovido,"foi banido da festa!")

#A terceira e última forma de remoção de item na lista se da pelo da função remove(). A diferença ao usar o remove é que nele você não passa o index que quer deletar e sim o valor do item que deseja deletar
viajando = "Henrrique"
convidados.remove(viajando)
print(convidados)
print(viajando,"não vai estar presente pois está viajando.")
#endregion

#region Organizando listas

#Para organizar uma lista esxiste três métodos, o sort, o sorted e o reverse
#O sort serve para organizar a lista em ordem alfabética ou numérica crescente ou decrescente. ATENÇÂO, o método sort não possui retorno ou seja não da pra desfazer a organização após aplicada
print("\n")

convidados2 = ['Isac','Guilherme','David','Pedro','Marcos','Heitor','Henrrique']
print(convidados2)

convidados2.sort()
print(convidados2)

#Ordem alfabética inversa
convidados2.sort(reverse=True)
print(convidados2)

#O sorted faz a mesma coisa que o sort porém ele ao invés de alterar a própria lista ele salva o resultado a organização em uma variável nova ou pode ser impresso direto no print(). Ou seja na lista original ainda é mantida a ordem bagunçada
print("\n")
convidados2 = ['Isac','Guilherme','David','Pedro','Marcos','Heitor','Henrrique']
print(convidados2)

print(sorted(convidados2))
print(convidados2)

#O reverse serve para colocar a lista em ordem cronológica reversa ou seja ele inverte a lista porém não coloca em ordem alfabética ou numérica
print("\n")
convidados2 = ['Isac','Guilherme','David','Pedro','Marcos','Heitor','Henrrique']
print(convidados2)
convidados2.reverse()

print(convidados2)
#endregion

#region Mais algumas Operações

#Para exibir o tamanho de uma lista ou seja quantos itens ela possui use a função len()
print("\n")
print(len(convidados2))

#Para criar uma lista de número de forma rápida use o comando list(range()) e passe em qual número inicia e qual número para. Lembre que o número que para não será exibido
print("\n")
numeros = list(range(1,5))
print(numeros) #1, 2, 3, 4

#Para ver qual é o maior valor de uma lista usa a função max() e para ver o menor valor use min()
print("\n")
print(max(numeros))
print(min(numeros))
#endregion

#region Matrizes

#Matriz basicamente é uma lista dentro de uma lista algo parecido como uma planilha em excell ou google sheets.
#Para criar uma matriz basta usar o mesmo conceito que foi usado para criar lista, porem cada item desta lista será também uma lista
print("\n")

timeXpessoas = [["Palmeiras","Flamengo","América","Cruzeiro","Atlético"],["José","Maria","Tiago","Pablo","Luana"]]

print(timeXpessoas)
print(timeXpessoas[1][2]) #vai acessar a lista no index 1 e vai acessar seu item no index 2
print(timeXpessoas[0][2]) #vai acessar a lista no index 0 e vai acessar seu item no index 2

#endregion