import base64
import hashlib
from Crypto.Cipher import AES

 

 #public key 
PASSWORD = 'a1b2c3d4e5f6g7h8'
# encrypted secret message
ENCRYPTED_MSG = b'3Jgrnid0Y+JrqsxpWZ0q3w3UqpH6GEy4Fh27thLMUM0A82fHf2D6sl7AboKFcyOA'
 
def decrypt(enc, password):
    #retrive private key 
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return cipher.decrypt(enc[16:])
 
 


 
# Let us decrypt using our original password
decrypted_msg = decrypt(ENCRYPTED_MSG, PASSWORD)
print(bytes.decode(decrypted_msg))