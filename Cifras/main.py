from ceaser import *
from vigenere import *
from sub import *
from trans import *


CeaserE(13)
vigE("lucasss")
subE()
transE(5)

CeaserD(13)
vigD("lucasss")
subD()
transD(5)

a1 = open("in.txt",'rb').read()
a2 = open("out_E_ceaser.txt",'rb').read()
a3 = open("out_E_vigenere.txt",'rb').read()
a4 = open("out_E_sub.txt",'rb').read()
a5 = open("out_E_trans.txt",'rb').read()

ceaserKey = AtaqueClaroCeaser(a1[0],a2[0])

print("Chave Ceaser:",ceaserKey)

vigenereKey = AtaqueClaroVigenere(a1,a3)

print("Chave de Vigenere:",bytes(vigenereKey).decode())

subKey = AtaqueClaroSub(a1,a4)

print("Chave de Substituicao:",subKey)

transKey = AtaqueClaroTrans(a5)

print("A chave", transKey, "e uma possivel candidata.")
