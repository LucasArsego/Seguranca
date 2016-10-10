def vigE(keyV):
	l = []
	arq = open("in.txt",'rb').read()
	out = open("out_E_vigenere.txt", "wb")
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
	arq = open("out_E_vigenere.txt",'rb').read()
	out = open("out_D_vigenere.txt", "wb")
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
