from Cryptodome.Cipher import AES
from Cryptodome.Hash import HMAC, SHA256
from Cryptodome.Random import get_random_bytes
import pprint

data = 'secret data to transmit'.encode()
# Tamaños de las claves de las Advaced Encryption Standard
aes_key = get_random_bytes(16)
hmac_key = get_random_bytes(16) # hash-based message authentication Code

cipher = AES.new(aes_key, AES.MODE_CTR)
# print(dir(cipher))  para ver el objeto su clases
ciphertext = cipher.encrypt(data)

nonce = cipher.nonce # Obtener objeto cipher 

hmac = HMAC.new(hmac_key, digestmod=SHA256)
tag = hmac.update(nonce + ciphertext).digest() # Actualizar el HMAC con el nonce y el textro cifrado, con .digest obtenemos el valor de HMAC

with open("encrypted.bin", "wb") as f:
    f.write(tag)
    f.write(nonce)
    f.write(ciphertext)
