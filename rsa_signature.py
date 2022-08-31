import rsa

HASH_ALGO = 'SHA-256'
def sign(msg, key):
    return rsa.sign(msg.encode('ascii'), key, HASH_ALGO)

def verify(msg, sig, key):
	try:
    		return rsa.verify(msg.encode('ascii'), sig, key) == HASH_ALGO
	except:
		return False

def get_key(filename, is_public_key):
	f = open(filename, 'rb')
	key = None
	if is_public_key:
		key = rsa.PublicKey.load_pkcs1( f.read() )
	else:
		key = rsa.PrivateKey.load_pkcs1( f.read() )
	f.close()
	return key



