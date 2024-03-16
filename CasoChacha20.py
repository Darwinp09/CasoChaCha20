#Pregunta1
#Desarrollar un programa en el lenguaje de programación de su preferencia que
#utilice alguna librería externa que implemente ChaCha20. Utiliza ChaCha20 para
#cifrar el siguiente mensaje utilizando los siguientes parámetros

#Programa:
from Crypto.Cipher import ChaCha20
import base64

#Parametros
texto_plano = "Este es un mensaje secreto que quiero cifrar."
clave = b'z\xe8~"\xcayW\x14g\x18+\x1c+\xf9\x80\x06P\x9ej\x888\xb4G\xdf\xe4\xc50,\x8dY\x80\x19'
nonce = b'\xd6\x7f6\xc7\xe8i*\xa4'
texto_cifrado = b'Ehq0\x83\xcb\x8fo\xab\xed\xd0S\x06\xcc\xbb\xecw\xe9\xec(\x1f\xc5E\xdb\x88\x18`W\xc3yQn\xad3\xec.\x08\x92\x8d\x8e\xbb%\x8f\x1a\xa6\xc9=\x15\x0f5\xaa'
texto_cifrado2 = b"\xad\xe2\x9a[C\xca\xa9\xadn\xf9\xaa)\x13\xc2X\x9e\x89\x19`C\xc4n\x1em\xf8?\xe7|\x0b\xd3\xdc\x8f\xacd\x85\x0c\xb8\xc3'\x1a\x12>"

# Cifrar
cipher = ChaCha20.new(key=clave, nonce=nonce)
ciphertext = cipher.encrypt(texto_plano.encode())
ciphertext_b64 = base64.b64encode(ciphertext)

# Descifrado 1
cipher = ChaCha20.new(key=clave, nonce=nonce)
texto_descifrado = cipher.decrypt(texto_cifrado).decode()

# Descifrado 2 
cipher = ChaCha20.new(key=clave, nonce=nonce)
cipher.seek(64)  # Desplazar el keystream 8 bytes
texto_descifrado2_1 = cipher.decrypt(texto_cifrado2)
texto_descifradoHEX = texto_descifrado2_1.hex()

# Resultados
print("Texto Cifrado:", ciphertext_b64.decode())
print("Texto Descifrado:", texto_descifrado)
print("Texto Descifrado HEX:", texto_descifradoHEX)

#Pregunta2: ¿Cuál es el texto cifrado resultante? 
#Respuesta: RWhxMIPLj2+r7dBTBsy77Hfp7CgfxUXbiBhgV8N5UW6tM+wuCJKfkrh3ig37


#Preguntas 3.A :¿Qué tamaño tiene el nonce que has utilizado para cifrar el texto plano?
#Respuesta: El nonce es de 8 BYTES


#3.B ¿Puede utilizar un nonce de mayor tamaño (ej. 12 bytes o 16 bytes)?
# Respuesta:
# Sí, puede utilizarce un nonce de 12 bytes, pero un nonce de 16 bytes es posible que no funcione de la misma manera o podría no ser compatible.

#3.C ¿Qué implicaciones de seguridad tiene utilizar un nonce de mayor tamaño?
# Respuesta:
# Un nonce más grande mejora la seguridad al hacer más difícil que se produzca tal coincidencia, especialmente en sistemas con un gran volumen de tráfico cifrado o que generan muchos nonces automáticamente.

# Pregunta 4:
# Añada al programa que han desarrollado la funcionalidad de descifrado. Use esta funcionalidad para descifrar el siguiente texto cifrado. Tengan en
# cuenta que se ha utilizado la misma clave y el mismo nonce que en el
# apartado anterior:
# b'Ehq0\x83\xcb\x8fo\xab\xed\xd0S\x06\xcc\xbb\xecw\xe9\xec(\x1f\xc5E\xdb\x88\x18`W\xc3yQn\xad3\xec.\x08\x92\x8d\x8e\xbb%\x8f\x1a\xa6\xc9=\x15\x0f5\xaa'

#¿Cuál es el texto plano resultante?
# Respuesta: 
# El texto resultante es el mismo que originalmente se cifro, debido a que usamos la misma clave y nonce en el cifrado y decifrado.

#Ppregunta5:
#Por último, suponemos que el receptor nos ha enviado un mensaje cifrado con la clave y el nonce mostrados anteriormente, sin embargo, se ha producido un error en la transmisión y se han perdido los 8 primeros bytes del texto cifrado. Esto supone que nuestro keystream y el del receptor no están sincronizados. El texto cifrado que hemos recibido es el siguiente:
#b"\xad\xe2\x9a[C\xca\xa9\xadn\xf9\xaa)\x13\xc2X\x9e\x89\x19`C\xc4n\x1em\xf8?\xe7|\x0b\xd3\xdc\x8f\xacd\x85\x0c\xb8\xc3'\x1a\x12>"

#Descifra el texto cifrado que se ha recibido. Recuerda el conceto de counter y busca el método de la librería ChaCha20 que estén utilizando para sincronizar el keystream con el del receptor. 

clave = b'z\xe8~"\xcayW\x14g\x18+\x1c+\xf9\x80\x06P\x9ej\x888\xb4G\xdf\xe4\xc50,\x8dY\x80\x19'
nonce = b'\xd6\x7f6\xc7\xe8i*\xa4'
texto_cifrado = b"\xad\xe2\x9a[C\xca\xa9\xadn\xf9\xaa)\x13\xc2X\x9e\x89\x19`C\xc4n\x1em\xf8?\xe7|\x0b\xd3\xdc\x8f\xacd\x85\x0c\xb8\xc3'\x1a\x12>"

# Ajustando para sincronizar con el receptor
cipher = ChaCha20.new(key=clave, nonce=nonce)
cipher.seek(64)  # desplaza 64bits = 8 bytes

# Descifrando el texto
texto_descifrado = cipher.decrypt(texto_cifrado)

# Mostrar el resultado
print("Texto Descifrado: ", texto_descifrado.hex())

#¿Cuál es el texto plano resultante?
# Respuesta: 
# El texto plano resultante es el mismo que se cifro en el principio.