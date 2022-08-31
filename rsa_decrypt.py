import rsa

ciphertext = b''

print("Ciphertext: ", ciphertext)

key_file = input("Key filename: ")
f = open(key_file, 'rb')

key = rsa.PrivateKey.load_pkcs1( f.read() )
plaintext = rsa.decrypt(ciphertext, key).decode('ascii')

print("Plaintext: ", plaintext)
