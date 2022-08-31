import rsa

key_file = input("Key filename: ")
plaintext = input("Plaintext: ")
f = open(key_file, 'rb')

key = rsa.PublicKey.load_pkcs1( f.read() )
ciphertext = rsa.encrypt(plaintext.encode('ascii'), key)

print("Ciphertext: ", ciphertext)



