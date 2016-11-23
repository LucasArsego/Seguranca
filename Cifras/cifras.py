import math
import os
import itertools

# Funções da cifra de ceaser.
def CeaserE(key,name,nameOut,op):
	arq = open(name,'rb').read()
	l = []
	k = key
	for x in arq:
		d = (x+k) % 256
		l.append(d)
	if op:
		open(nameOut,"wb").write(bytes(l))
	else:
		return bytes(l)

def CeaserD(key,name,nameOut,op):
	arq = open(name,'rb').read()
	l = []
	k = key
	for x in arq:
		d = (x-k) % 256
		l.append(d)
	if op:
		open(nameOut,"wb").write(bytes(l))
	else:
		return bytes(l)


def AtaqueClaroCeaser(nameArq1,nameArq2):
	arq1 = open(nameArq1,'rb').read()
	arq2 = open(nameArq2,'rb').read()
	print("Chave possivel para a cifra de Ceaser(Ataque Claro):",(arq2[0] - arq1[0]))



def AtaqueEscuroCeaser(name,nameOut):
	all_words = open("all_words.txt",'rb').read()
	all_words = all_words.split()
	arq = open(name,'rb').read()
	for key in range(1,10**5):
		words = bytes((t - key) % 256 for t in arq)
		lista_palavras = words.split()
		l = []
		for w in lista_palavras:
			if w in all_words:
				l.append(w)
		if len(l) > int(len(arq)/7):
			open(nameOut,"wb").write(bytes((t - key) % 256 for t in arq))
			print("Chave provavel para a cifra de Ceaser(Ataque Escuro): ",key)
			return
# Funções da cifra de Substituicao.

def subE(nameKey,name,nameOut,op):
	l = []
	arq = open(name,'rb').read()
	V = open(nameKey,'rb').read()
	for x in arq:
		d = V[x]
		l.append(d)
	if op:
		open(nameOut,"wb").write(bytes(l))
	else:
		return bytes(l)

def subD(nameKey,name,nameOut,op):
	l = []
	arq = open(name,'rb').read()
	V = open(nameKey,'rb').read()
	for x in arq:
		for y in V:
			if V[y] == x:
				d = y
				l.append(d)
	if op:
		open(nameOut,"wb").write(bytes(l))
	else:
		return bytes(l)


def AtaqueClaroSub(nameArq1,nameArq2):
	arq1 = open(nameArq1,'rb').read()
	arq2 = open(nameArq2,'rb').read()
	l = {}
	for i in range(len(arq1)):
		l[arq1[i]] = arq2[i]

	lista = [ 0 for i in range(256)]

	for i in range(256):
		if i in l:
			lista[i] = l[i]
	print("Chave possivel para a cifra de Substituicao(Ataque Claro):",lista)


# Funções da cifra de vigenere.

def vigE(keyV,name,nameOut,op):
	l = []
	arq = open(name,'rb').read()
	V = keyV
	V = V.encode()
	i = 0
	k = []
	for j in arq:
		k.append((j + V[i]) % 256)
		i += 1
		if i >= len(V):
			i = 0
	if op:
		open(nameOut,"wb").write(bytes(k))
	else:
		return bytes(k)

def vigD(keyV,name,nameOut,op):
	l = []
	arq = open(name,'rb').read()
	V = keyV
	V = V.encode()
	i = 0
	k = []
	for j in arq:
		k.append((j - V[i]) % 256)
		i +=1
		if i >= len(V):
			i = 0
	if op:
		open(nameOut,"wb").write(bytes(k))
	else:
		return bytes(k)

def AtaqueClaroVigenere(nameArq1,nameArq2):
	arq1 = open(nameArq1,'rb').read()
	arq2 = open(nameArq2,'rb').read()
	l = []
	for i in range(len(arq1)):
		l.append((arq2[i]- arq1[i]))
	print("Chave possivel para a cifra de Vigenere(Ataque Claro):",bytes(l).decode())


def AtaqueEscuroVigere(nameArq):
	arq = open(nameArq,'rb').read()
	all_words = open("all_words.txt",'rb').read()
	all_words = all_words.split()
	c = itertools.permutations('a0123456789',3) #ABCDEFGHIJKLMNOPQRSTUVWXYZ
	for i in c:
		a = ''.join(i)
		lista_palavras = vigD(a,nameArq,'Saidas/out_D_vig_escuro.txt',0)
		lista_palavras = lista_palavras.split()
		d = []
		for w in lista_palavras:
			if w in all_words:
				d.append(w)
		if len(d) > int(len(arq)/7):
			vigD(a,nameArq,'Saidas/out_D_vig_escuro.txt',1)
			print("Chave provavel para a cifra de Vigenere(Ataque Escuro):",a)
			return

# Funções da cifra de Transposição

def transE(key,name,nameOut,op):
	arq = open(name,'rb').read()
	linhas = key
	bir = os.path.getsize(name)
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
	if op:
		open(nameOut,"wb").write(bytes(l))
	else:
		return bytes(l)
def transD(key,name,nameOut,op):
	arq = open(name,'rb').read()
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
		open(nameOut,"wb").write(bytes(l))
	else:
		return bytes(l)

def AtaqueClaroTrans(nameArq1,nameArq2):
	arq1 = open(nameArq1,'rb').read()
	for i in range(1,len(arq1)):
		arq = transD(i,nameArq1,"x.txt",0)
		arq2 = open(nameArq2,'rb').read()
		if arq[0:100] == arq2[0:100]:
			print("Chave possivel para a cifra de Transposicao(Ataque Claro):", i)


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
			print("Chave provavel para a cifra de Transposicao(Ataque Escuro):", i)
			return
