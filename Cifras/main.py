from ceaser import *
from vigenere import *

CeaserE()
vigE()
vigD()
CeaserD()

a1 = open("in.txt",'rb').read()
a2 = open("out_E_ceaser.txt",'rb').read()
a3 = open("out_E_vigenere.txt",'rb').read()

ceaserKey = AtaqueClaroCeaser(a1[0],a2[0])
print("Chave Ceaser:",ceaserKey)

vigenereKey = AtaqueClaroVigenere(a1,a3)

print("Chave de Vigenere:",bytes(vigenereKey).decode())
