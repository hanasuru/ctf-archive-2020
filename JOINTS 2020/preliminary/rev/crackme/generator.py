import random

operations="+ - *".split(" ")
serial="745UI-82JFS-9KNDB-CBJO7-OUM4G"
serial=''.join(serial.split('-'))

print(serial)

x={}

while len(set(x.keys()))!=len(serial)*2:
	index1 = random.randint(0,len(serial)-1)
	chosen1=ord(serial[index1])
	index2 = random.randint(0,len(serial)-1)
	chosen2 = ord(serial[index2])
	if(chosen1 < chosen2):
		indexmax = index2
		indexmin = index1
		ma = chosen2
		mi = chosen1
	else:
		indexmax = index1
		indexmin = index2
		ma=chosen1
		mi=chosen2

	op = random.choice(operations)
	res = "{} {} {}".format(str(ma),op,str(mi))
	res = "{}".format(eval(res))

	eq = "solver.add(s[{}] {} s[{}] == {})".format(str(indexmax),op,str(indexmin),res)

	tup = (indexmax, op, indexmin)
	if(tup not in x.keys()):
		x[tup] = eq

eqs = list(x.values())
random.shuffle(eqs)
for eq in eqs:
	print(eq)

# for i in x:
# 	chosen1=ord(serial[i])
# 	index2 = random.randint(0,len(shuffle)-1)
# 	chosen2 = ord(serial[index2])
# 	if(chosen1 < chosen2):
# 		indexmax = index2
# 		indexmin = i
# 		ma = chosen2
# 		mi = chosen1
# 	else:
# 		indexmax = i
# 		indexmin = index2
# 		ma=chosen1
# 		mi=chosen2

# 	op = random.choice(operations)
# 	res = "{} {} {}".format(str(ma),op,str(mi))
# 	res = "{}".format(eval(res))

# 	eq = "solver.add(s[{}] {} s[{}] == {})".format(str(indexmax),op,str(indexmin),res)
# 	#eq = "s[{}] {} s[{}] == {}".format(str(indexmax),op,str(indexmin),res)
# 	print(eq)

# x = list(range(len(serial)))
# random.shuffle(x)
# for i in x:
# 	chosen1=ord(serial[i])
# 	shuffle=serial
# 	index2 = random.randint(0,len(shuffle)-1)
# 	chosen2 = ord(shuffle[index2])
# 	if(chosen1 < chosen2):
# 		indexmax = index2
# 		indexmin = i
# 		ma = chosen2
# 		mi = chosen1
# 	else:
# 		indexmax = i
# 		indexmin = index2
# 		ma=chosen1
# 		mi=chosen2

# 	op = random.choice(operations)
# 	res = "{} {} {}".format(str(ma),op,str(mi))
# 	res = "{}".format(eval(res))

# 	eq = "solver.add(s[{}] {} s[{}] == {})".format(str(indexmax),op,str(indexmin),res)
# 	#eq = "s[{}] {} s[{}] == {}".format(str(indexmax),op,str(indexmin),res)
# 	print(eq)