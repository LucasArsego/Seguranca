def subE():
	l = []
	arq = open("in.txt",'rb').read()
	out = open("out_E_sub.txt", "wb")
	V = open("key1",'rb').read()
	for x in arq:
		d = V[x]
		l.append(d)
	out.write(bytes(l))
	out.close()

def subD():
	l = []
	arq = open("out_E_sub.txt",'rb').read()
	out = open("out_D_sub.txt", "wb")
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
