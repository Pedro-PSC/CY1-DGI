import chatBrain as cb

nome_maquina = 'Dieguinho'
cb.saudacoes(nome_maquina)
while True:
    texto = cb.recebeTexto()
    resposta = cb.buscaResposta(nome_maquina,texto)
    if cb.exibeResposta(resposta,nome_maquina) == 'fim':
        break