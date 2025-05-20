#region Básico de Strings

#Strings é o nome que damos os textos na programação

#em uma variável do tipo string você pode armazenar textos de diversos tamanhos como

#uma palavra
string1 = "Oi!"

#uma frase
string2 = 'Oi, tudo bem?'

#Pode se usar aspas simples '' ou aspas duplas "" em python para armazenar strings

#Para imprimir uma string pode se adicionar o texto diretamente na função print() ou pode passar a variável que com a string para a função
print(string1)
print(string2)
print('Tudo bem e você')

#Caso você queira saltar linhas em um texto utilize o comando \n (a '\' se encontra ao lado esquerdo da tecla 'z')

print("Saltando \n\n linhas \n")

#Utiliize o \t para acrescentar espaços maiores em um texto
print("Olá\tCtrl=Play!")
#endregion

#region Index de strings

#Use a função len() para ver quantos caracteres formam a string
frase = 'Ctrl+Play - Escola de programação e robótica'
qntfrase = len(frase)
print(qntfrase)

nome = "Pedro Paulo Sousa do Couto"

#Toda string possui in index (indice), o index ele é o valor de posição de cada caractere
#Imprimindo a primeira letra do variável nome
print(nome[0])
#Usamos os '[]' para controlar qual posição desejamos operar. Lembrar que o index sempre começa do valor 0

#Para imprimir a partir de um caractere insira : após um valor de posição Ex.: [:7]
print(nome[6:]) #Paulo Sousa do Couto

#Para imprimir até um caractere insira : antes do valor de posição Ex.: [7:]
print(nome[:6]) #Pedro

#Para imprimir uma parte específica coloque um valor de posição de início antes do : e um valor de parada depois dos : Ex.: [7:16]
print(nome[6:18]) #Paulo Sousa

#Caso queira imprimir do fim para o início use valores negativos no index. Vale lembrar que neste caso como não existe o número -0 o index então começa pelo -1
print(nome[-1]) #o

print(nome[:-15]) #Pedro Paulo

#Usa [::] para imprimir a string saltando caracteres
print(nome[::2])

#Use a função find() para encontrar a posição do index do caractere que deseja 
email = 'fulano@ctrlplay.com.br'
print(email.find('@'))

#Use a função count() para contar quantas vezes o mesmo caractere repete na string
print(email.count('.'))
#endregion

#region Operação Com Strings

#Strigs são imutáveis ou seja após sua criação você não pode alterar o valor de um caractere específico
#teste = 'imutabilidade'
#teste[0] = 'm'

#Concatenação - Usada para unir duas strings em uma só
nome = "James"
sobrenome = "Bond"
print(nome+' '+sobrenome)

#Repetição - Usada para imprimir a mesma string x vezes
print(sobrenome*7)

#Para converter outro tipo de variável para string pasta usar a função str()
numeroDeIrmaos = 2
print('Você têm '+str(numeroDeIrmaos)+' irmãos')

#Métodos de Strings

#Para transformar uma string inteira em caixa alta
print(frase.upper())

#Para transformar uma string inteira em caixa baixa
print(frase.lower())

#Use split para divir a string em seções
cadaPlavra = frase.split()
print(frase)
print(cadaPlavra)

#Pode informar ao slplit qual o parâmetro da divisão passando o caractere nos parenteses
cadaPlavra = frase.split(' - ')
print(cadaPlavra)
print(cadaPlavra[0])
print(cadaPlavra[1])
#endregion

#Para Inputar informações no sistema basta usar a função input()

nome_completo = input("Digite seu nome completo: ")
print('\nOlá '+nome_completo)