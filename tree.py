from bitarray import *

def addprefixos(xs, p):
    return dict((k, bitarray(p) + v) for (k,v) in xs.items())


class N:
    def __init__(self, x, f):
        self.x = x
        self.f = f
        self.l = None
        self.r = None

    def join(self, o):
        n = N(None, self.f + o.f)
        n.l = self
        n.r = o
        return n

    def coding(self):
        l = {}
        r = {}
        if self.x:
            return {self.x: bitarray()}
        if self.l:
            l = self.l.coding()
        if self.r:
            r = self.r.coding()
        ret = {}
        ret.update(addprefixos(l, '0'))
        ret.update(addprefixos(r, '1'))
        return ret

    def __lt__(self, o):
        return self.f > o.f

    def __repr__(self):
        return "N('%s',%d)" % (self.x, self.f)

def huffmann(l):
    while(len(l) > 1):
        l.sort()
        a = l.pop()
        b = l.pop()
        c = a.join(b)
        l.append(c)
    return l.pop().coding()

def countT(txt):
    l = {}
    for i in txt:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1
    return l

def createNode(lista):
    l = []
    for x, j in lista.items():
        l.append(N(x,j))
    return l

def countF(k):
    total = 0
    for x, j in k.items():
        total = total + j
    return total

def createIntro(lista):
    k = {}
    for x, j in lista.items():
        k[x] = (countF(lista) / j)
    return k

texto = "meu texto eh esse texto aqui"

dfrequencia = countT(texto)
dIntro = createIntro(dfrequencia)
l = createNode(dfrequencia)

print(dIntro)
print()
print(huffmann(l))
