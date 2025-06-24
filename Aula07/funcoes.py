# Funções são algoritmos com o objetivo de executar uma cadeia de comando que podem/vão se repetir várias vezes no programa em tempos indeterminados fazendo assim não ter a nescessidade de recriar o algoritmo toda vez que precisar repeti-lo apenas chamando a função para ser executada.

# Para criar uma função vasta digitar o comando 'def' logo em seguida passar o nome da função e colocar o '()' e finalizar a linha com ':' EX.> def Pular():

# Dica: Tente diferenciar suas funções de variáveis como por exemplo fazendo usas função sempre começar com letra maiúscula e suas variáveis sempre com letras minúsculas

def Boas_Vindas():
    print('Bem-Vindo à Ctrl+Play')

# Para executar uma função basta chama-la pelo nome dela da seguinte forma

Boas_Vindas()
Boas_Vindas()
Boas_Vindas()

# Os paranteses de uma função é a região de parâmetros, que são informações que a função precisa para ser executata, como por exemplo uma função de soma necessita de dois números para poder realizar os cálculos


def Saudacao(nome,sobrenome):
    print(f'Saudações {nome} {sobrenome} como está a aula de hoje?')

Saudacao('Pedro','Couto')

def Velocidade(distancia,tempo=1.5):
    velocidade = distancia/tempo
    print(f'A sua velocidade foi de {velocidade:.2f} Km/h')

d = int(input('Digite quantos Km de distância foi percorrido: '))
t = int(input('Digite em quantas horas fez o percurso: '))

Velocidade(d,t)

# Valor arbitrário é quando você quer passar para uma função vários vlores porém não sabe a quantidade exata de valores que vai passar, para isso basta colocar o '*' antes do nome do parâmetro

def Prepara_Acai(*ingredientes, tamanho='medio'):
    print(f'Preparando um açaí {tamanho} com os seguintes ingredientes adicionais: ')
    for i in ingredientes:
        print(f'- {i}')

Prepara_Acai('banana','granola')
Prepara_Acai('morango','kiwi','leite em pó', tamanho='grande')
Prepara_Acai('banana',tamanho='pequeno')
Prepara_Acai()

# Funções compostas são funções que chamam outras funções em suas definições

def Menor(lista):
    menorValor = lista[0]
    for x in lista:
        if(x < menorValor):
            menorValor = x
    return menorValor

def Maior(lista):
    maiorValor = lista[0]
    for x in lista:
        if(x > maiorValor):
            maiorValor = x
    return maiorValor

def Maior_menor(lista):
    print(f'Maior valor da lista: {Maior(lista)}')
    print(f'Menor valor da lista: {Menor(lista)}')

Maior_menor([4,5,6,2,1,3])

# Função Recursiva são funções que dentro da sua definição elas chamam a si mesma para ser executada

def Dobra_Lencol(lencol:int, gaveta:int):
    if(lencol < gaveta):
        return 0
    else: 
        return 1 + Dobra_Lencol(lencol/2 , gaveta)
    
l = Dobra_Lencol(200,25)
print(l)