from cryptography.fernet import Fernet
file=open('key.key','rb')
key=file.read()
file.close()
with open('cyphertext.txt','rb') as f:
    data=f.read()
fernet=Fernet(key)
encrypted=fernet.encrypt(data)
with open('cyphertext.txt','wb') as f:
    f.write(encrypted)
