import base64

# ============= ENCODING ============= #

b64_info = input("What sentence do you want to encode?:")
b64_enc = b64_info.encode('ascii')

b64_encode = base64.b64encode(b64_enc)
b64_d = b64_encode.decode('ascii')

print(f"Encoded Value:{b64_d}")

# ============= DECODING ============ #

b64_e = b64_d.encode('ascii')

b64_decode = base64.b64decode(b64_e)
b64_dec_ascii = b64_decode.decode('ascii')

print(f'Decoded Value:{b64_dec_ascii}')