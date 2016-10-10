import math
import os
def transE(keyT):
	arq = open("in.txt",'rb').read()
	out = open("out_E_trans.txt", "wb")
	key = keyT
	linhas = key
	bir = os.path.getsize("in.txt")
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

def transD(keyT):
	arq = open("out_E_trans.txt",'rb').read()
	out = open("out_D_trans.txt", "wb")
	key = keyT
	linhas = key
	bir = os.path.getsize("in.txt")
	colunas = math.ceil(bir/key)
	mat = [ [] for x in range(colunas)]
	k = 0
	for j in arq:
		mat[k].append(j)
		k += 1
		if k >= colunas:
			k = 0

	l = []
	for i in	 mat:
		for j in i:
			l.append(j)
	out.write(bytes(l))
	out.close()

def AtaqueClaroTrans(arq1):
	for i in range(1,len(arq1)):
		transE(i)
		arq = open("out_E_trans.txt",'rb').read()
		if arq1[0:100] == arq[0:100]:
			return i
