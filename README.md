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

