ex = int(input("Escolha qual dos exercícios deseja executar:\n\n1 → Tabuada\n2 → Maior da Lista\n3 → Fibonacci\n\n"))

print('\n')

# O 'match case' é um comando semelhante as condicionais de 'if', 'elif' e 'else', porém ele verifica apenas casos de igualdade de um único objeto apenas, Ex.: if ex == 1. Usá-lo para esses casos torna o código mais legível e prático ao invés de usar o 'if'. Sua estrutura base funciona da seguinte forma, em 'match' insira qual valor que será usado para parâmetro de comparação, dentro dele cada 'case' terá qual será o posivel caso de igualdade, e dentro de cada 'case' o código que você quer que execute quando este caso for verdadeiro.

match ex:
    case 1:
        print("Faça um programa que recebe um número de 1 a 10 e imprime a tabuada desse número.\n\n")
        n = int(input("Insira um número de 1 a 10: "))
        
        if n > 0 and n < 11:      
            i = 1
            print(f'Tabuada do {n}:\n')
            while i < 11:
                print(f'{n} x {i} =',(n*i))
                i+=1
            else:
                print('\nFim da Tabuada!')
        else:
            print('\nValor inválido')
    
    case 2:
        print('Faça um programa que recebe do usuário 10 valores de números inteiros, armazena em um vetor(lista) e após percorrê-lo exibe qual é o maior valor e a sua posição.\n\n')
        
        numeros = []

        print('Insira 10 números')

        i = 1
        while i < 11:
            valor=int(input(f'Digite o {i}º número: '))
            numeros.append(valor)
            i += 1

        maior_valor = numeros[0]
        posicao_maior_valor = 0

        # Use enumerate() sempre que você estiver iterando sobre uma lista (ou qualquer outra sequência) e precisar saber qual é a posição atual do item no loop.
        for indice, valor_atual in enumerate(numeros):
            if valor_atual > maior_valor:
                maior_valor = valor_atual
                posicao_maior_valor = indice
        
        print(f'\nOs números digitados foram: {numeros}')
        print(f'\nO maior valor digitado é: {maior_valor}')
        print(f'\nA posição do maior valor digitado é: {posicao_maior_valor+1}')
    
    case 3:
        print('A sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nesta sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.\n\n')

        n = int(input("Digite um número inteiro entra 1 e 45: "))

        if n <=0 or n >=46:
            print("Valor inválido")
        else:
            fib = [0,1] #Início da sequencia de fibonacci
            for i in range(2,n):
                prox_num = fib[i-1] + fib[i-2]
                fib.append(prox_num)

            print(", ".join(map(str,fib[:n])))
            # map() é útil quando você precisa transformar cada elemento de uma coleção de dados de uma maneira uniforme.
            # join() é perfeito para criar uma string formatada a partir de uma lista de strings, controlando o que aparece entre cada elemento.