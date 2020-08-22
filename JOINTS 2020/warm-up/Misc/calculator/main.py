#!/usr/bin/env python3

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

import sys
import random

sys.stdout = Unbuffered(sys.stdout)

correct=0
print("20 corrects = flag")
op = list("+-*")
while correct<20:

    num1 = random.randint(0,1000)
    num2 = random.randint(0,1000)
    op= random.choice(op)
    res = eval("{} {} {}".format(num1,op,num2))

    try:
        ans = int(input("{} {} {} = ".format(num1,op,num2)))
        if(ans==res):
            correct+=1
            print("correct")
        else:
            print("incorrect")
    except ValueError:
        print("incorrect")

print("JOINTS20{Simple_Arithmetic}")