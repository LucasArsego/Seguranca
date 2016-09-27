def CeaserE(arqName,outName,k):
	arq = open(arqName,'rb').read()
	out = open(outName, "wb")
	l = []	
	for x in arq:
		d = (x+k) % 256
		l.append(d)
	out.write(bytes(l))
	out.close()
def CeaserD(arqName,outName,k):
	out = open(arqName, "rb").read()
	out2 = open(outName, "wb")
	l = []
	for x in out:
		d = (x-k) % 256
		l.append(d)
	out2.write(bytes(l))
	out2.close()
