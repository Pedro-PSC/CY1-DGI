import math

def AreaQuadrado():
    u = input('\nInsira a unidade de medida: ')
    l = float(input('Insira qual o tamanho do lado do quadrado: '))
    r = print(f'\nA área do quadrado com lado de {l}{u} é de: {(l*l):.2f}{u}²')
    return r

def AreaTriangulo():
    u = input('\nInsira a unidade de medida: ')
    b = float(input('Insira qual o tamanho do base do triângulo: '))
    a = float(input('Insira qual o tamanho do altura do triângulo: '))
    r = print(f'\nA área do triângulo com base de {b}{u} e altura de {a}{u} é de: {((b*a)/2):.2f}{u}²')
    return r

def AreaCirculo():
    u = input('\nInsira a unidade de medida: ')
    raio = float(input('Insira qual o tamanho do raio do círculo: '))
    r = print(f'\nA área do círculo com raio de {raio}{u} é de: {(math.pi*(raio**2)):.2f}{u}²')
    return r

def VolumeCubo():
    u = input('\nInsira a unidade de medida: ')
    l = float(input('Insira qual o tamanho do lado do quadrado: '))
    r = print(f'\nA área do quadrado com lado de {l}{u} é de: {(l**3):.2f}{u}³')
    return r

def VolumeTriangulo():
    u = input('\nInsira a unidade de medida: ')
    b = float(input('Insira qual o tamanho do base do triângulo: '))
    a = float(input('Insira qual o tamanho do altura do triângulo: '))
    r = print(f'\nA área do triângulo com base de {b}{u} e altura de {a}{u} é de: {((b*a)/2):.2f}{u}³')
    return r