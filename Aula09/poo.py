# POO → Programação Orientada á Objetos (OOP)
# O POO vem com o objeto de tratar tudo da programação como um objeto, ou seja, você abstrair algo ou uma idéia do mundo real e tentar aplica-la no mundo virtual.

# Classes → são representações ou modelos abstratos de entidades e situações do mundo real.

class Cachorro():
    # Atributos → características deste objeto

    #Método inicializador → serve para que as informações que compõem os atributos venham de fora da classe
    def __init__(self, _raca, _idade, _peso, _genero, _nome):
        self.raca = _raca
        self.idade = _idade
        self.peso = _peso
        self.genero = _genero
        self.nome = _nome

    #Métodos → ações/funções realizadas por este objeto
    def movimentar(self):
        pass

    def alimentar(self):
        pass

    def dormir(self):
        pass

    def latir(self):
        pass

    def ficha(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nRaça: {self.raca}\nGenero: {self.genero}'
    
    #Métodos Getters → métodos que pegam a informação da classe
    def getRaca(self):
        return self.raca
    def getIdade(self):
        return self.idade
    def getPeso(self):
        return self.peso
    def getGenero(self):
        return self.genero
    def getNome(self):
        return self.nome
    
    #Métodos Setters → métodos que inseri as informações nos atributos da classe
    def setRaca(self,r):
        self.raca = r
    def setIdade(self,i):
        self.idade = i
    def setPeso(self,p):
        self.peso = p
    def setGenero(self,g):
        self.genero = g
    def setNome(self,n):
        self.nome = n

#Criando o objeto
dog1 = Cachorro(_nome='Rex',_idade='5',_peso='25kg',_genero='M',_raca='Pastor Alemão')
dog2 = Cachorro(_nome='Mel',_idade='10',_peso='8kg',_genero='F',_raca='Poodle')

print(dog1.ficha())
print('\n')
print(dog2.ficha())

print('\n')
print(dog1.getIdade())
dog1.setIdade('8')
print(dog1.getIdade())

print('\n\n')

class Livro():
    def __init__(self, _titulo, _autor, _paginas):
        print("Um livro foi criado")
        self.titulo = _titulo
        self.autor = _autor
        self.paginas = _paginas

    def __str__(self):
        return f'Titulo: {self.titulo}\nAutor: {self.autor}\nPaginas: {self.paginas} páginas'
    
    def __len__(self):
        return self.paginas
    
    def __del__(self):
        print("Livro destruido")

# Assim que o livro for instanciado será executado o método __init__()
book = Livro('POO As Terças', 'Pedro Paulo', 267)

# Método Especiais
# Dispara o método __str__()
print(book)

# Dispara o método __len__()
print(len(book))

# Dispara o método __del__()
del book
print(book)