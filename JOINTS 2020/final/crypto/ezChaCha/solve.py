from pwn import *
from itertools import permutations
import random


for loop in range(10):
    r=process("./ezChaCha.py")
    # r=remote("127.0.0.1",8891)
    r.recvuntil("Agent id ")

    #get seed
    SEED=int(r.recvline().strip())

    r.recvuntil("Select menu:"),
    r.sendline('1')
    r.recvline()

    #get Enc.Data
    ENC=r.recvline().strip().decode("hex")
    # print "Seed : "+str(SEED)
    # print "Encrypted Data : "+ENC.encode("hex")

    random.seed(SEED)

    padList=[]

    for i in range(3):
        padList.append(random.randint(1,10)**2)

    # get the original Flag Length
    lengthEncrypted=len(ENC)-sum(padList)

    #list padding permutations
    perms=list(permutations(padList))

    #temporary data for encryption to find out the key
    tmp1='a'*lengthEncrypted

    r.recvuntil("Select menu:")
    r.sendline('2')
    r.recvuntil(">> ")
    r.sendline(tmp1)
    encTmp1=r.recvline().strip()

    # find out the key
    key=xor(tmp1,encTmp1.decode("hex"))

    tmpFlag=""
    found=0
    # print perms
    # print "key: " +str(len(key))

    for perm in perms:
        tmpFlag=""
        tmpFlag=ENC[perm[0]:perm[2]]
        tmpFlag=tmpFlag[lengthEncrypted/2+perm[1]:]+tmpFlag[:lengthEncrypted/2]
        tmpFlag=xor(key,tmpFlag)
        print tmpFlag

# $ python solve.py | strings # try to find printable string
# Result
# """
# Salsa20_and_Cha
# aP$28
# Salsa20_and_Cha
# ZZp*
# Cha_are_similar
# """







