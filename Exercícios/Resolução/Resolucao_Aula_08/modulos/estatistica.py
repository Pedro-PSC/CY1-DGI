from collections import Counter

def Media():
    soma = 0
    lista_num =[]

    total_num = int(input('\nQuantos números você deseja inserir: '))

    for i in range(total_num):
            num = float(input(f'Digite o {i+1}º número: '))
            lista_num.append(num)
            soma += num
    
    if total_num > 0:
        media = soma / total_num
        r = print(f'\nA média dos números {(', '.join(map(str,lista_num)))} é: {media}')
        return r
    else:
        r = print(f'\nNenhum número foi inserido para calcular a média.')
        return r
        


def Moda():
    numeros = []
    i=0
    print('\nInsira os números um por um. digite "fim" quando terminar para calcular')

    while True:
        entrada = input(f'Digite o {i+1}º número ou "fim": ').strip().lower()

        if entrada == 'fim':
            break
        else:
            if '.' in entrada:
                 numero = float(entrada)
            else:
                 numero = int(entrada)
            numeros.append(numero)
    
    if not numeros:
         print('\nNenhum número foi inserido para calcular.')
         return

    cont_num = Counter(numeros)
    frequencia_maxima = 0

    if cont_num:
         frequencia_maxima = max(cont_num.values())

    modas = [num for num, count in cont_num.items() if count == frequencia_maxima]

    if len(modas) == len(cont_num) and len(modas) > 1:
         r = print('\nTodos os números aparecem com a mesma frequência. Não há moda')
         return r
    elif len(modas) == 1:
         r = print(f'\nA moda é: {modas[0]}')
         return r
    else:
         r = print(f'\nAs modas são: {', '.join(map(str,modas))}')
         return r