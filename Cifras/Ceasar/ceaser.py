
arq = open("/home/aluno-local/Documentos/UFFS_Lucas/Seguranca/Cifras/inputs/1.input",'rb').read()

k = 17

a = input()
l = []

if a == 'e':
	out = open("1_e.output", "wb")
	for x in arq:
		d = (x+k) % 256
		l.append(d)
	out.write(bytes(l))
	out.close()
if a == 'd':
	out = open("1_e.output", "rb").read()
	out2 = open("1_d.output", "wb")
	for x in out:
		d = (x-k) % 256
		l.append(d)
	out2.write(bytes(l))
	out2.close()
