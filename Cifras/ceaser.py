def CeaserE(arqName,outName,k):
	arq = arqName
	out = open("out_E_ceaser.txt", "wb")
	l = []
	for x in arq:
		d = (x+k) % 256
		l.append(d)
	out.write(bytes(l))
	out.close()
def CeaserD(arqName,outName,k):
	out = arqName
	out = open("out_D_ceaser.txt", "wb")
	l = []
	for x in out:
		d = (x-k) % 256
		l.append(d)
	out2.write(bytes(l))
	out2.close()
