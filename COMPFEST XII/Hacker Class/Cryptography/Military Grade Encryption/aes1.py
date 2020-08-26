

from Crypto.Cipher import AES
import hashlib

IV = "iniIVbukanflagya"
KEY = hashlib.md5(open('key.txt', 'rb').read()).hexdigest()
flag = open('flag.txt', 'rb').read()
not_flag = open('not_flag.txt', 'rb').read()


def unpad(data):
	return data[:-ord(data[-1])]

def pad(data):
	length = 16 - (len(data) % 16)
	return data + bytes([length])*length

def encrypt(message):
	aes = AES.new(KEY, AES.MODE_OFB, IV)
	message = pad(message)
	enc = aes.encrypt(message)
	return enc

def decrypt(encrypted):
	aes = AES.new(KEY, AES.MODE_OFB, IV)
	return unpad(aes.decrypt(encrypted))
	
open('flag.enc', 'wb').write(encrypt(flag))
open('not_flag.enc', 'wb').write(encrypt(not_flag))