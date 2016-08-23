import Crypto
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

arq = open("msg.txt", "rb")

hash = arq.read(32)

hashcriptografado = arq.read(128)

public = arq.read(162)

key = RSA.importKey(public)

if key.encrypt(hashcriptografado,1024)[0] == hash:
    print()    
    print("Funciona BIIIR!!")
else:
    print()
    print("Nao vai dar!!!!!")

print()
print("Teste com outra chave publica!!")
print()

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) 
publickey = key.publickey()

if publickey.encrypt(hashcriptografado,1024)[0] == hash:
    print("Funciona BIIIR!!")
    print()
else:
    print("Nao vai dar!!!!!")
    print()
