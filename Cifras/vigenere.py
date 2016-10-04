def vigE(arqName,outName,V):
	l = []
	arq = arqName
	out = open("out_E_vigenere.txt", "wb")
	i = 0
	k = []
	for j in arq:
		k.append((j + V[i]) % 256)
		i += 1
		if i >= len(V):
			i = 0
	out.write(bytes(k))
	out.close()

def vigD(arqName,outName,V):
	l = []
	arq = arqName
	out = open("out_D_vigenere.txt", "wb")
	i = 0
	k = []
	for j in arq:
		k.append((j - V[i]) % 256)
		i +=1
		if i >= len(V):
			i = 0
	out.write(bytes(k))
	out.close()
