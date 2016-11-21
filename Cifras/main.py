from cifras import *

#CeaserE(8)
#vigE("lucasss")
#subE()

#CeaserD(8)
#vigD("lucasss")
#subD()

#a1 = open("inputs/in.txt",'rb').read()
a2 = open("Saidas/out_E_ceaser.txt",'rb').read()
a3 = open("Saidas/out_E_vigenere.txt",'rb').read()
a4 = open("Saidas/out_E_sub.txt",'rb').read()
a5 = open("Saidas/out_E_trans.txt",'rb').read()
a6 = open("inputs/7.input.ceasar.X",'rb').read()
a7 = open("inputs/7.input.transp.X",'rb').read()

#ceaserKey = AtaqueClaroCeaser(a1[0],a2[0])

#print("Chave Ceaser:",ceaserKey)

#vigenereKey = AtaqueClaroVigenere(a1,a3)

#print("Chave de Vigenere:",bytes(vigenereKey).decode())

#subKey = AtaqueClaroSub(a1,a4)

#print("Chave de Substituicao:",subKey)

transKey = AtaqueClaroTrans(a7)

print("A chave", transKey, "e uma possivel candidata.")

#AtaqueEscuroCeaser(a6)

#AtaqueEscuroVigere(a6)

AtaqueEscuroTrans("inputs/7.input.transp.X")
