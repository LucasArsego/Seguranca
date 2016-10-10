def CeaserE(keyV):
	arq = open("in.txt",'rb').read()
	out = open("out_E_ceaser.txt", "wb")
	l = []
	k = keyV
	for x in arq:
		d = (x+k) % 256
		l.append(d)
	out.write(bytes(l))
	out.close()

def CeaserD(keyV):
	arq = open("out_E_ceaser.txt",'rb').read()
	out = open("out_D_ceaser.txt", "wb")
	l = []
	k = keyV
	for x in arq:
		d = (x-k) % 256
		l.append(d)
	out.write(bytes(l))
	out.close()


def AtaqueClaroCeaser(arq1,arq2):
	return arq2 - arq1
