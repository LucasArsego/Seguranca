privateKey = int(input("Chave privada: "))

mod = 23
base  = 5

print("Resultado:",(base ** privateKey) % mod)

res = int(input("Chave Intermediaria: "))

print("RESULTADO:",(res**privateKey) % mod)



