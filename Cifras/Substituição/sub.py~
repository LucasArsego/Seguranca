l = []
V = open("/home/aluno-local/Documentos/UFFS_Lucas/Seguranca/Cifras/key1",'rb').read()

a = input()

if a == 'e':
	arq = open("/home/aluno-local/Documentos/UFFS_Lucas/Seguranca/Cifras/inputs/1.input",'rb').read()
	out = open("1_e.output", "wb")
	for x in arq:
		d = V[x]
		l.append(d)

	out.write(bytes(l))
	out.close()
if a == 'd':
	arq = open("1_e.output",'rb').read()
	out = open("1_d.output", "wb")
	for x in arq:
		for y in V:
			if V[y] == x:
				d = y
				l.append(d)
	out.write(bytes(l))
	out.close()


