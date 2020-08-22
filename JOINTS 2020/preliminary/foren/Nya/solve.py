text=open("./chall.txt","r").read()

text=text.split(" ")

traverse={"nya":"00","Nya":"01","NYA":"11","NYa":"10"}
    
print text
hasil=""
for char in text:
    try:
        hasil+=traverse[char]
    except:
        pass
print len(hasil)
print hasil

FLAG=""
for bit in range(0,len(hasil),8):
    FLAG+=chr(int(hasil[bit:bit+8],2))
print FLAG