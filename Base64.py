import base64

b64_info = input("What sentence do you want to encode?:")
b64_enc = b64_info.encode('ascii')

b64_encode = base64.b64encode(b64_enc)
b64_d = b64_encode.decode('ascii')

print(f"Encoded Value:{b64_d}")