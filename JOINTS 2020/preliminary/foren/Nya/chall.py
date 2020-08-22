#!/usr/bin/python

def padding(binary):
    res='0'*(8-len(binary))+binary
    return res

def main():

    FLAG="JOINTS20{Nya_nya_NYa_nya_nYaaaaa}"

    soal="""
Nya may be short for Nyaneng or other names.
A Nya is usually a kind humorous and beautiful person.
You are very lucky if you have a Nya as a friend.
Nyas don't have many friends but they have very strong relationships with their friends.
Nyas are very shy at first but are outgoing and loud when you get to know them.
They can say just one thing and it will brighten your day.
They always know how to cheer you up and always have your back.
Nyas are also GORGEOUS.
They may sometimes be insecure but are mostly very confident.
Nyas are skinny but really strong and athletic.
If you have a Nya don't lose . FLAG:"""+FLAG

    print soal
    BIN = ''.join(padding(format(ord(i), 'b')) for i in soal)
    print len(BIN)

    mapping={"00":"nya","01":"Nya","11":"NYA","10":"NYa"}
    text=""
    for i in range(0,len(BIN),2):
        text+=mapping[BIN[i:i+2]] + " "
    print text
    print BIN

    f=open("./chall.txt","w")
    f.write(text)
    f.close()

if __name__ == "__main__":
    main()