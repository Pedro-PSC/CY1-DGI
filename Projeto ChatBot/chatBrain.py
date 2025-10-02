#region TERMINAL
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
#endregion

#region GUI
def exibeResposta_GUI(resposta, nome):
    return resposta.replace("Chatbot",nome)
    
def saudacao_GUI(nome):
    import random
    frases = ["Bom dia! Meu nome é " + nome + ". Como vai você?", "Olá!", "Oi, tudo bem?"]
    return frases[random.randint(0,2)]

def salva_sugestao(sugestao):
    with open("Projeto ChatBot\BaseDados.txt","a+") as conhecimento:
        conhecimento.write("Chatbot: " + sugestao + "\n")
        
def buscaResposta_GUI(texto):
    with open("Projeto ChatBot\BaseDados.txt","a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if jaccard(texto,viu) > 0.3:
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                conhecimento.write('\n' + texto)
                return "Me desculpe, não sei o que falar"
            
def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase)<1: return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum/(len(textoBase.split()))
    
def limpa_frase(frase):
    tirar = ["?","!","...",".",",","Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase
#endregion