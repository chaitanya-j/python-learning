from Crypto.Cipher import AES
key = b'sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX) 



nonce = cipher.encrypt()
ciphertext, tag = cipher.encrypt_and_digest(data)