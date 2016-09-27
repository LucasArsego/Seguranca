def subE(arqName,outName,V):
	l = []	
	arq = open(arqName,'rb').read()
	out = open(outName, "wb")	
	for x in arq:
		d = V[x]
		l.append(d)
	out.write(bytes(l))
	out.close()

def subD(arqName, outName,V):
	l = []	
	arq = open(arqName,'rb').read()
	out = open(outName, "wb")
	for x in arq:
		for y in V:
			if V[y] == x:
				d = y
				l.append(d)
	out.write(bytes(l))
	out.close()


