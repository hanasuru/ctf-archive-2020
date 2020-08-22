import random

def dec(x,file):
	w=open(file,'rb')
	e=w.read()[6:-6]
	res=""
	for i in range(len(e)):
		res+=chr(e[i]^ord(x[i]))
	return res

random.seed(1588427220-1)
one=""
for i in range(100085):
	one+=chr(random.randint(0,255))
random.seed(1588427220)
two=""
for i in range(100085):
	two+=chr(random.randint(0,255))
random.seed(1588427220+1)
three=""
for i in range(100085):
	three+=chr(random.randint(0,255))

w= open('sv.pdf','wb')
w.write(dec(two,"flag.pdf.enc").encode("charmap"))
#print(dec(two,"flag.pdf.enc"))
w.close()
