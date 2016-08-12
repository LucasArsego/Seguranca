from Crypto.Cipher import AES
text = "BIIIIIIIIIIIIIIR"
IV = "Eh HORA DO SHOOW"
key = "1234567891098765"

obj = AES.new(key, AES.MODE_CBC, IV)

ciphertext = obj.encrypt(text)
print(ciphertext)

obj2 = AES.new(key, AES.MODE_CBC,IV)
ciphertext = obj2.decrypt(ciphertext)
a = ciphertext.decode()
print(a)
