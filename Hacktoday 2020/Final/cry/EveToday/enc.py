import hashlib
import random
import math
import os
from Crypto.Signature import pkcs1_15
from Crypto.Util.Padding import *
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Hash import MD5
from gmpy2 import *
from time import *



def DH(p,shared_key,iv):
	print("[+] Encrypt Flag")
	sleep(1)
	print("p = ",p,"\n")
	
	flag = open('flag.txt','rb').read()
	key = hashlib.sha256(str(shared_key).encode()).hexdigest()[48:]

	return (iv , AES.new(key.encode(), AES.MODE_CBC, iv).encrypt(pad(flag,16)))


def Alice(m):
	print("[+]--- INTERCEPT ALICE---")
	sleep(1)

	e=0x10001
	p=##CORRUPTED
	q=##CORRUPTED
	n = p*q
	c = pow(m,e,n)

	banner="""
                 **
                ***
               ****
           z  *****
             ***L** y
            *******
           ********
          *********
              x 
	"""
	print(banner)

	x=p+q
	y=p-q
	z_kuadrat= (x**2)+(y**2)
	print("z_kuadrat : ", z_kuadrat)
	Luas= (x*y)/2
	
	print("Luas   	  : ",int(Luas))
	return{"cipher_A":c}


def Bob(m):
	print("[+]--- INTERCEPT BOB---\n")
	sleep(1)
	print("! ! ! WARNING ! ! !")
	print("""
    !!!!!!!!!!!!!!!!!!!!!!!
    !  Hacker detected !! !
    !!!!!!!!!!!!!!!!!!!!!!!""")

	bobpass=int(input("[+] Verification \n[+]Bob's Password: "))
	yours=int(input("[+]Verification code : "))

	if(bobpass==yours or size(bobpass)>1024 or size(yours)>1024):
		return("You're not Bob !!")

	if(hashlib.md5(long_to_bytes(bobpass)).hexdigest()==hashlib.md5(long_to_bytes(yours)).hexdigest()):
		return hex(m)
	else:
	    return {"error": "Verification failed"}


if __name__ == "__main__":
	list =##CORRUPTED ([ , ],[ , ] ...)
	couple_chosen = random.choice(list)
	## Pilih pasangan bilangan random dari sample yg sudah diuji coba pada soal dibuat agar menghindari beberapa hal jika benar benar pure random tanpa pengecheckan dahulu, 
	#  anggap aja generate random number
	alice = couple_chosen[0] 
	bob = couple_chosen[1] 

	g = 2
	p = getPrime(64)
	A = pow(g,alice,p)
	B = pow(g,bob,p)
	shared_key = pow(B,alice,p)
	iv = os.urandom(16)

	print("Hi eve !\nLooking for Alice and Bob's conversation again today?")
	while(1):
		print("""
___________________________________
| Menu :                           |
|       1. Intercept Alice         |
|       2. Intercept Bob           |
|       3. Encrypt Flag            |
|__________________________________|

""")
		inp=input("Select : ")

		if(int(inp)==1):
			print(Alice(A),"\n")

		elif(int(inp)==2):
			print("\nReceive from Bob : ",Bob(B))	

		elif(int(inp)==3):
			eevee, enc_flag = DH(p,shared_key,iv)
			print("iv : ",eevee.hex())
			print("enc_flag : ",enc_flag.hex())
			print("\n\n")

		else:
			print("PILIHAN TIDAK TERSEDIA")
			exit()