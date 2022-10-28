from Crypto.Cipher import  AES
from secrets import token_bytes # Рандомный генератор ключа

key = token_bytes(16) # Длинна ключа

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX) # Шифрованный текст
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode("UTF-8"))
    return nonce, ciphertext, tag

def decrypt(nonce,ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce) # Шифрованный текст
    plaintext = cipher.decrypt(ciphertext) # Текст
    try:
        cipher.verify(tag)
        return plaintext.decode("UTF-8")
    except:
        return False
nonce, ciphertext, tag = encrypt(input('Введите сообщение :'))
plaintext = decrypt(nonce, ciphertext, tag)
print(f'Зашифрованное сообщение : {ciphertext}')
if not plaintext:
    print("Сообщение поврежденно")
else:
    print(f'Разшифрованное сообщение : {plaintext}')