import hashlib

st = "Hi this is  Chaitanya"
print(hashlib.algorithms_guaranteed)

print(hashlib.sha256(bytes(st,'utf-8')).hexdigest())
