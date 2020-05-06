from cryptography.fernet import Fernet
file = open('key.key','rb')
key=file.read()
print(key)
