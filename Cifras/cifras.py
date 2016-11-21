import math
import os
import itertools

# Funções da cifra de ceaser.
def CeaserE(keyV):
	arq = open("inputs/in.txt",'rb').read()
	out = open("Saidas/out_E_ceaser.txt", "wb")
	l = []
	k = keyV
	for x in arq:
		d = (x+k) % 256
		l.append(d)
	out.write(bytes(l))
	out.close()

def CeaserD(keyV):
	arq = open("Saidas/out_E_ceaser.txt",'rb').read()
	out = open("Saidas/out_D_ceaser.txt", "wb")
	l = []
	k = keyV
	for x in arq:
		d = (x-k) % 256
		l.append(d)
	out.write(bytes(l))
	out.close()


def AtaqueClaroCeaser(arq1,arq2):
	return arq2 - arq1


def AtaqueEscuroCeaser(arq):
    all_words = open("all_words.txt",'rb').read()
    all_words = all_words.split()

    for key in range(1,10**5):
        words = bytes((t - key) % 256 for t in arq)
        lista_palavras = words.split()

        l = []
        for w in lista_palavras:
            if w in all_words:
                l.append(w)

        if len(l) > 0:
            open("Saidas/out_D_ceaser_escuro.txt","wb").write(bytes((t - key) % 256 for t in arq))
            print("Chave: ",key)
            break

# Funções da cifra de Substituicao.

def subE():
	l = []
	arq = open("inputs/in.txt",'rb').read()
	out = open("Saidas/out_E_sub.txt", "wb")
	V = open("key1",'rb').read()
	for x in arq:
		d = V[x]
		l.append(d)
	out.write(bytes(l))
	out.close()

def subD():
	l = []
	arq = open("Saidas/out_E_sub.txt",'rb').read()
	out = open("Saidas/out_D_sub.txt", "wb")
	V = open("key1",'rb').read()
	for x in arq:
		for y in V:
			if V[y] == x:
				d = y
				l.append(d)
	out.write(bytes(l))
	out.close()


def AtaqueClaroSub(arq1,arq2):
	l = {}
	for i in range(len(arq1)):
		l[arq1[i]] = arq2[i]

	lista = [ 0 for i in range(256)]

	for i in range(256):
		if i in l:
			lista[i] = l[i]

	return lista

# Funções da cifra de vigenere.

def vigE(keyV):
	l = []
	arq = open("inputs/in.txt",'rb').read()
	out = open("Saidas/out_E_vigenere.txt", "wb")
	V = keyV
	V = V.encode()
	i = 0
	k = []
	for j in arq:
		k.append((j + V[i]) % 256)
		i += 1
		if i >= len(V):
			i = 0
	out.write(bytes(k))
	out.close()

def vigD(keyV):
	l = []
	arq = open("Saidas/out_E_vigenere.txt",'rb').read()
	out = open("Saidas/out_D_vigenere.txt", "wb")
	V = keyV
	V = V.encode()
	i = 0
	k = []
	for j in arq:
		k.append((j - V[i]) % 256)
		i +=1
		if i >= len(V):
			i = 0
	out.write(bytes(k))
	out.close()

def AtaqueClaroVigenere(arq1,arq2):
	l = []
	for i in range(len(arq1)):
		l.append((arq2[i]- arq1[i]))
	return l


def AtaqueEscuroVigere(arq):
	pass

# Funções da cifra de Transposição

def transE(keyT):
	arq = open("outputs/7.input",'rb').read()
	out = open("Saidas/out_E_trans.txt", "wb")
	key = keyT
	linhas = key
	bir = os.path.getsize("outputs/7.input")
	colunas = math.ceil(bir/key)
	mat = [ [] for x in range(linhas)]
	k = 0
	falta = colunas - bir%colunas
	arq = list(arq) + [0] * falta
	for j in arq:
		mat[k].append(j)
		k += 1
		if k >= linhas:
			k = 0

	l = []
	for i in mat:
		for j in i:
			l.append(j)
	out.write(bytes(l))
	out.close()

def transD(keyT,name,nameOut,op):
	arq = open(name,'rb').read()
	out = open(nameOut, "wb")
	key = keyT
	linhas = key
	bir = os.path.getsize(name)
	colunas = math.ceil(bir/key)
	mat = [ [] for x in range(colunas)]
	k = 0
	for j in arq:
		mat[k].append(j)
		k += 1
		if k >= colunas:
			k = 0
	l = []
	for i in mat:
		for j in i:
			l.append(j)
	if op:
		out.write(bytes(l))
		out.close()
	else:
		return bytes(l)

def AtaqueClaroTrans(arq1):
	for i in range(1,len(arq1)):
		transE(i)
		arq = open("Saidas/out_E_trans.txt",'rb').read()
		if arq1[0:100] == arq[0:100]:
			return i


def AtaqueEscuroTrans(nameArq):
	arq = open(nameArq,'rb').read()
	all_words = open("all_words.txt",'rb').read()
	all_words = all_words.split()

	for i in range(1,os.path.getsize(nameArq)):
		lista_palavras = transD(i,nameArq,"a.txt",0)
		lista_palavras = lista_palavras.split()
		d = []
		for w in lista_palavras:
			if w in all_words:
				d.append(w)
		if len(d) > 100:
			transD(i,nameArq,"Saidas/out_D_trans_escuro.txt",1)
			print("Chave:", i)
			return
