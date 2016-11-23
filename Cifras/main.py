from cifras import *


a1 = "inputs/in.txt"
a2 = "Saidas/out_E_ceaser.txt"
a3 = "Saidas/out_E_vigenere.txt"
a4 = "Saidas/out_E_sub.txt"
a5 = "Saidas/out_E_trans.txt"
a6 = "inputs/7.input.ceasar.X"
a7 = "inputs/7.input.transp.X"
a8 = "inputs/6.input.vig.X"
a9 = "outputs/6.input"
a0 = "outputs/7.input"
print("Resultados Ataque em Claro:")
print()
AtaqueClaroCeaser(a0,a6)
AtaqueClaroVigenere(a9,a8)
AtaqueClaroSub(a1,a4)
AtaqueClaroTrans(a7,a0)

print()
print("Resultados Ataque em Escuro:")
print()
AtaqueEscuroCeaser(a6,"Saidas/out_D_ceaser_escuro.txt")
AtaqueEscuroVigere('inputs/7.input.vig.X')
AtaqueEscuroTrans(a7)
