import math 
import os

a = input()
key = 5

if a == 'e':
	arq = open("1.input",'rb').read()
	out = open("1_e.output", "wb")
	linhas = key
	bir = os.path.getsize("1.input")
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
if a == 'd':
	arq = open("1_e.output",'rb').read()
	out = open("1_d.output", "wb")
	linhas = key
	colunas = math.ceil(os.path.getsize("1_e.output")/key)
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
