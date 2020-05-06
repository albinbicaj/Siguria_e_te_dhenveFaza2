from cryptography.fernet import Fernet
file=open('key.key','rb')
key=file.read()
file.close()
message="Takimi mbahet te premten ne ora 11:00"
encoded = message.encode()
f=Fernet(key)
encrypted=f.encrypt(encoded)
print(encrypted)
