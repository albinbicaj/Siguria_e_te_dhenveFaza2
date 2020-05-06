import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password_provided = "password"
password = password_provided.encode()
salt = b'\x01M9\xf5\x02NUc\xf2U\xb3\xb231\x10\xf9'
kdf = PBKDF2HMAC(
algorithm=hashes.SHA256(),
length=32,
salt=salt,
iterations=100000,
backend=default_backend()
    )
key=base64.urlsafe_b64encode(kdf.derive(password))
print(key)
