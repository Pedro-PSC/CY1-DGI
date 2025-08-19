import unittest
from operacoes import sobrenome_ordem, Prova


class NomeTest(unittest.TestCase):
    def test_sobrenome_ordem(self):
        nomeCompleto = sobrenome_ordem('João','Madureira','Silva')
        self.assertNotEqual(nomeCompleto, "Maria Rosa Chaves")

class ProvaTest(unittest.TestCase):
    def setUp(self):
        self.questao = 'Qual a área da floresta Amazônica?'
        self.resposta = '6.7 milhões de km²'
        self.p = Prova()
        self.p.armazena_QR(self.questao,self.resposta)

    def test_armazenaQuestao(self):
        # testa se uma questão foi armazenada de forma correta
        self.assertIn('Qual a área da floresta Amazônica?', self.p.questoes)

    def test_armazenaResposta(self):
        # testa se uma resposta foi armazenada de forma correta
        self.assertIn('6.7 milhões de km²', self.p.respostas)

unittest.main(argv=[''], exit=False)

'''
MÉTODO                      |   VERIFICAÇÃO
assertEqual(a,b)            |   a == b
assertNotEqual(a,b)         |   a != b
assertTrue(x)               |   x é verdadeiro
assertFalse(x)              |   x é falso
assertIn(item, lista)       |   item está na lista
assertNotIn(item, lista)    |   item não está na lista
'''