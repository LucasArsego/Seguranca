
arq = open("/home/aluno-local/Documentos/UFFS_Lucas/Seguranca/Cifras/inputs/1.input",'rb').read()

k = 17

out = open("1.output", "wb")

l = []

for x in arq:
	d = (x+k) %256
	l.append(d)

out.write(bytes(l))
out.close()
