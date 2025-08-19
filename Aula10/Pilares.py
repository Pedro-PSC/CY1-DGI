# Os Quatro Pilares do POO

#1º → Abstração
## A abstração é o ato de abstrair um objeto ou uma idéia do mundo real e passar ele para mundo virtual. OBS.: É extremamente importante levar o contexto do seu software na hora de abstrair uma idéia

#2º → Encapsulamento
## O encasulamento é uma forma de segurança dentro do POO, ela esconde/priva um elemento ao seu escopo impedindo o acesso deste mesmo elemento de forma externa como se fosse uma caixa preta.
## Na programação os elementos eles podem ser de dois status diferentes, sendo eles públicos ou privados. Um elemento é um elemento que pode ser ascessado em qualquer escopo, já os elementos privados são elementos que possuem uma segurança maior pois você controla qual escopo tem ascesso a esse elemento

class A():
    a = 1 # atributo público
    __b = 2 # atributo privado a class A

class B(A):
    __c = 3 # atributo privado de B

    def __init__(self):
        print(self.a)
        print(self.__c)

objA = A()
print(objA.a) # imprimir 1

objB = B()
#print(objB.b)
#print(objB.__c)

#3º → Herança
## A herança é o ato de uma classe receber os dados de atributos e métodos de uma outra classe.

class Animal():
    def __init__(self):
        print("Animal Criado")

    tamanho = ''
    energia = ''
    fome = ''
    velocidade = ''

    def crescer(self):
        return print('Crescendo...')
    def dormir(self):
        return print('Dormindo...')
    def comer(self):
        return print('Comendo...')
    def movimentar(self):
        return print('Movimentando...')
    
class AnimalSelvagem():

    tamanho = ''
    energia = ''
    fome = ''
    velocidade = ''

    def cacar(self):
        return print('Caçando...')
    def corre(self):
        return print('Correndo...')

class Felinos(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Felino Criado")

    som = ''
    dieta = ''
    especie = ''

    def sonorizar(self):
        return print('Som...')
    def roronar(self):
        return print('Roronando...')
    
class Onca(Felinos,AnimalSelvagem):
    def __init__(self):
        print('Onça criada')

leao = Felinos()
leao.dormir()

onca_pintada = Onca()
onca_pintada.cacar()

print('\n')
#4º → Polimorfismo
## O poliformismo é a capacidade de uma classe alterar algum dado que foi herdado

class vovo():
    corOlho = 'Castanho'

class papai(vovo):
    marcaNascenca = 'Pinta na costas'

class filho(papai):
    corOlho = 'Verde'
    marcaNascenca = 'Pinta na costas e mancha na perna'

avo = vovo()
pai = papai()
eu = filho()

print(f'a cor do olho do meu avo é {avo.corOlho}')
print(f'a cor do olho do meu pai é {pai.corOlho}')
print(f'a cor do meu olho é {eu.corOlho}')
print(f'meu pai tem uma marca de nascença, {pai.marcaNascenca}')
print(f'eu tenho uma marca de nascença, {eu.marcaNascenca}')