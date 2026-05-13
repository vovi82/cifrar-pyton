from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generar una clave y un vector de inicialización (IV)
key = os.urandom(32)  # AES-256 requiere una clave de 32 bytes
iv = os.urandom(16)  # El tamaño del IV para AES es de 16 bytes

# Mensaje a cifrar
plaintext = b'La clave esta en tu Corazon'

# Crear un cifrador AES en modo CFB
cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()

# Cifrar el mensaje
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

print(f'Clave: {key.hex()}')
print(f'IV: {iv.hex()}')
print(f'Texto cifrado: {ciphertext.hex()}')

# Para descifrar, crear un nuevo cifrador AES en modo CFB con la misma clave e IV
decryptor = cipher.decryptor()
decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

print(f'Texto descifrado: {decrypted_text.decode()}')
