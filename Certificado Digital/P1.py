import Crypto
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) 
publickey = key.publickey()

msg = open("bambam.jpg",'rb').read()

hash = SHA256.new(msg).digest()

hashcriptografado = key.decrypt(hash)

arq = open("msg.txt", "wb")
arq.write(hash)
arq.write(hashcriptografado)

arq.write(publickey.exportKey("DER"))



