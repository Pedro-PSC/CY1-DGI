print('Ctrl+Play')
'''
x = int(input("digite um número: "))
y = input("digite outro número: ")

print(int(x)/int(y))
'''
# Exceções são uma forma de lidar com possíveis erros futuros que pode acontecer no seu código, para isso a gente uma estrutra chamada try except. A vantagem de usar esse recurso é que se bem aplicado ao ocorrer um erro no seu código o seu programa não vai mais travar/parar.

'''
try:
    Você tenta fazer algo aqui.
except Exceção1:
    Se causar a Exceção1, roda isso.
except Exceção2:
    Se causar a Exceção2, roda isso.
else: #Não é obrigatório ter um else
    Se não causa excessões, roda isso
'''

try:
    f = open('arquivo.txt', 'r')
    f.write("tente escrever isto")
except IOError:
    # Isso só irá verificar se há uma exceção IOError e,
    # em seguida, executar esta declaração de impressão
    print("Não foi possível localizar o arquivo")
else:
    print("Texto escrito com sucesso!")
    f.close()

print('O programa continou rodando')

# finally

'''
try:
    tenta fazer algo
finally:
    este bloco de código sempre é executado
'''

try:
    f = open('arquivo','r')
    f.write('Uma nova escrita')
except IOError:
    # Isso só irá verificar se há uma exceção IOError e,
    # em seguida, executar esta declaração de impressão
    print("Não foi possível localizar o arquivo")
finally:
    print('Sempre executa os comandos do bloco finally')

def perguta_numero():
    numero = 1
    while True:
        try:
            val = int(input("Entre um inteiro: "))
        except:
            print("Parece que você não digitou um inteiro")
            continue
        else:
            print('Muito Bem!!!')
            break
        finally:
            print('Tentativa número: ', numero)
            numero = numero + 1

perguta_numero()

print('Programa voltando a rodar normalmente')