# PRUEBAS PARA DESENCRIPTAR CONTRASEÑAS LOCALES DE GOOGLE

Hemos realizado diferentes pruebas e instalaciones de paquete módulos. Pero seguimos sin obtener resultados utiles, vamos a implementar un entorno virtual.
Para crearlo usaremos 

```bash

python -m venv <nombre_entorno>

```

Una vez realizado esto para activalor debemos de ejecutar <b> &lt;nombre_carpeta&gt;\Script\active.cmd</b> es un cmd que se ejecuta 

![alt text](image.png)

En nuestro CMD debemos de ver la opción de <i>myenv</i>. Cuando tengamos nuestro entorno activado debemos de instalar el siguiente paquete:

```bash

pip install pycryptodomex

```

Y para comprobar que todo está bien usaremos:

```bash

pip install pycryptodome-test-vectors
python -m Cryptodome.SelfTest

```

## PRUEBAS CON AES

Ahora realizaremos pruebas encriptación de datos para hacer esta pruebas tenemos una variable con un texto dentro del texto. Este archivo .py la función principal es encriptar la variable y almacenarlo en nuestro fichero que llamaremos <i>encrypted.bin</i> Este código lo podemos encontrar en <a href="https://pycryptodome.readthedocs.io/en/latest/src/examples.html">PyCrytoDome</a> en la página oficial se muestra un código bastante ambiguo y que no es compatible con pytho v3.11.4.

Lo he tenido que adaptar para el buen funcionamiento y pruebas 

```python

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

```





