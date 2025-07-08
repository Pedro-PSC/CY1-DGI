import math

def Soma():
    x = float(input('\nInsira o primeiro valor a ser somado: '))
    y = float(input('Insira o segundo valor a ser somado: '))
    r = print(f'\nO resultado da soma entre {x} e {y} é: {x+y}')
    return r

def Subtracao():
    x = float(input('\nInsira o primeiro valor a ser subtraido: '))
    y = float(input('Insira o valor a ser subtraido do primeiro número: '))
    r = print(f'\nO resultado da subtração entre {x} e {y} é: {x-y}')
    return r

def Multiplicacao():
    x = float(input('\nInsira o primeiro valor a ser multiplicado: '))
    y = float(input('Insira o valor a que irá multiplcar o primeiro valor: '))
    r = print(f'\nO resultado da multiplicação entre {x} e {y} é: {x*y}')
    return r

def Divisao():
    x = float(input('\nInsira o dividendo: '))
    y = float(input('Insira o divisor: '))
    r = print(f'\nO resultado da divisão entre {x} e {y} é: {x/y}')
    return r

def Porcentagem():
    x = float(input('\nInsira o valor total: '))
    y = float(input('Insira a porcentagem: '))
    r = print(f'\nO resultado de {y}% de {x} é: {x*(y/100)}')
    return r

def Potencia():
    x = float(input('\nInsira o valor da base: '))
    y = float(input('Insira o valor do expoênte: '))
    r = print(f'\nO resultado da potência de {x} elevado a {y} é: {x**y}')
    return r

def RaizQuadrada():
    x = float(input('\nInsira o valor que deseja descobrir a raiz quadrada: '))
    r = print(f'\nO resultado da raiz quadrada de {x} é: {math.sqrt(x)}')
    return r