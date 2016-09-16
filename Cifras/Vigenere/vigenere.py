V = "1234".encode()
l = []

a = input()

if a == 'e':
	arq = open("1.input",'rb').read()
	out = open("1_e.output", "wb")
	i = 0
	k = []
	for j in arq:
		k.append((j + V[i]) % 256)
		i += 1
		if i >= len(V):
			i = 0
	out.write(bytes(k))
	out.close()
if a == 'd':
	arq = open("1_e.output",'rb').read()
	out = open("1_d.output", "wb")
	i = 0
	k = []
	for j in arq:
		k.append((j - V[i]) % 256)
		i +=1
		if i >= len(V):
			i = 0
	out.write(bytes(k))
	out.close()
