import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from base64 import b64decode

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) 

publickey = key.publickey()

encrypted = publickey.encrypt(32, 3)

print ('encrypted message:', encrypted)

decrypted = key.decrypt(encrypted)

print ('decrypted', decrypted)

