# Primeira função saudando o usuário
def saudacoes(nome):
    import random
    frases = [f"Bom dia! Meu nome é {nome} Como vai você?", "Olá", "Oi, tudo bem?"]
    print(frases[random.randint(0,2)])

# Função que recebrá uma mensagem do usuário para depois responder com base nos dados
def recebeTexto():
    texto = "Cliente: " + input("Cliente: ")
    palavraProibida = ['vai tomar no cú', 'filho da puta', 'retardado']
    for p in palavraProibida:
        if p in texto:
            print("Não diga isso! Me respeite!")
            return recebeTexto()
        return texto

# Busca com base no texto do usuário a melhor resposta para dar ao cliente
def buscaResposta(nome, texto):
    with open("Projeto ChatBot\BaseDados.txt", 'a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("Cliente: ","") == "Tchau":
                    print(f'{nome}: volte sempre')
                    return 'fim'
                elif viu.strip() == texto.strip():
                    proximaLinha = conhecimento.readline()
                    if "Chatbot: " in proximaLinha:
                        return proximaLinha
            
            else:
                print("Me desculpe, não sei o que falar")
                conhecimento.write(f'\n{texto}')
                resposta_user = input("O que você esperava?\n")
                conhecimento.write(f"\nChatbot: {resposta_user}")
                return "Hum..."

# Exibe a resposta achada na busca
def exibeResposta(resposta,nome):
    print(resposta.replace("Chatbot",nome))
    if resposta == 'fim':
        return 'fim'
    return 'continua'