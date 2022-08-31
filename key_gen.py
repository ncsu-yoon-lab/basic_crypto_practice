import rsa
(publicKey, privateKey) = rsa.newkeys(1024)
f = open('pub_key.pem', 'wb')
f.write(publicKey.save_pkcs1('PEM'))
f.close()
f = open('prv_key.pem', 'wb')
f.write(privateKey.save_pkcs1('PEM'))
f.close()

