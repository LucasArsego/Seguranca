palavras = "bola, bala, casa, rosa, faca, fofa, fofo, abacate"
palavras = palavras.split(', ')
palavras_padroes = {}
for i in palavras:
    c = 0
    palavra_padrao = {}
    padrao = ''
    for j in i:
        if c == 0:
            palavra_padrao[j] = c
            padrao += str(c)
            c += 1
        elif j not in palavra_padrao:
            palavra_padrao[j] = c
            padrao += str(c)
            c += 1
        elif j in palavra_padrao:
            padrao += str(palavra_padrao[j])
    palavras_padroes[i] = padrao
print(palavras_padroes)
