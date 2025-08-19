# retorna um nome com os sobrenomes em ordem de tamanho

def sobrenome_ordem(nome, sobrenome1, sobrenome2):
    if(len(sobrenome2) > len(sobrenome1)):
        return nome+' '+sobrenome1+' '+sobrenome2
    else:
        return nome+' '+sobrenome2+' '+sobrenome1

print(sobrenome_ordem('José','Dias','Saraiva'))
print(sobrenome_ordem('João','Madureira','Silva'))
print(sobrenome_ordem('Pedro','Sousa','Couto'))

class Prova():
    def __init__(self):
        self.questoes = []
        self.respostas = []
    
    def mostra_questoes(self):
        print(self.questoes)
    
    def mostra_respostas(self):
        print(self.respostas)
    
    def armazena_QR(self,novaQ,novaR):
        self.questoes.append(novaQ)
        self.respostas.append(novaR)