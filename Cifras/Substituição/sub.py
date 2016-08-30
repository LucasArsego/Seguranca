
arq = open("/home/aluno-local/Documentos/UFFS_Lucas/Seguranca/Cifras/inputs/1.input",'rb').read()

out = open("1.output", "wb")

l = []
V = open("/home/aluno-local/Documentos/UFFS_Lucas/Seguranca/Cifras/key2",'rb').read()

print(V)

for x in arq:
	d = V[x]
	l.append(d)

out.write(bytes(l))
out.close()
