import hashlib

result = hashlib.sha256(bytes('Hi my name is Chaitanya!','utf-8'))
print(result.hexdigest())

