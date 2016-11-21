from cifras import *

CeaserE(8)
vigE("lucasss")
subE()

CeaserD(8)
vigD("lucasss","Saidas/out_E_vigenere.txt","Saidas/out_D_vigenere.txt",1)
subD()

a1 = open("inputs/in.txt",'rb').read()
a2 = open("Saidas/out_E_ceaser.txt",'rb').read()
a3 = open("Saidas/out_E_vigenere.txt",'rb').read()
a4 = open("Saidas/out_E_sub.txt",'rb').read()
a5 = open("Saidas/out_E_trans.txt",'rb').read()
a6 = open("inputs/7.input.ceasar.X",'rb').read()
a7 = open("inputs/7.input.transp.X",'rb').read()
a8 = open("inputs/6.input.vig.X",'rb').read()
a9 = open("outputs/6.input",'rb').read()
a0 = open("outputs/7.input",'rb').read()

ceaserKey = AtaqueClaroCeaser(a0[0],a6[0])
print("Chave possivel para a cifra de Ceaser(Ataque Claro):",ceaserKey)

vigenereKey = AtaqueClaroVigenere(a9,a8)
print("Chave possivel para a cifra de Vigenere(Ataque Claro):",bytes(vigenereKey).decode())

subKey = AtaqueClaroSub(a1,a4)
print("Chave possivel para a cifra de Substituicao(Ataque Claro):",subKey)

transKey = AtaqueClaroTrans(a7)
print("Chave possivel para a cifra de Trasposicao(Ataque Claro):", transKey)

AtaqueEscuroCeaser(a6)
AtaqueEscuroVigere('inputs/7.input.vig.X')
AtaqueEscuroTrans("inputs/7.input.transp.X")
