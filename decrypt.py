# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 03:31:23 2019

@author: user
"""
import Crypto
import hashlib
publicKey = 'a1b2c3d4e5f6g7h8'
encrypted = b'3Jgrnid0Y+JrqsxpWZ0q3w3UqpH6GEy4Fh27thLMUM0A82fHf2D6sl7AboKFcyOA'
private_key = hashlib.sha256(publicKey.encode("utf-8")).digest()

encoded = base64.b64encode(encrypted)
decoded = base64.b64decode(encoded)
print(decoded)