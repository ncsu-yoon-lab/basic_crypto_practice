import rsa

message = input("Enter message: ")
hash = rsa.compute_hash(message.encode(), 'SHA-256')
print("Hash: ", hash)