import random ,time ,os
def enc (O000OO0OO00000O00 ):
  OO0000OOOO0O0O0OO =open (O000OO0OO00000O00 ,'rb')
  OOOO0O000OO0O00OO =open (O000OO0OO00000O00 +'.enc','wb')
  O00O0O000O0O0OOOO =int (time .time ())
  random .seed (O00O0O000O0O0OOOO )
  OOOO0O000OO0O00OO .write (b"ransom")
  OOOOO00O0000OOO00 =""
  for O0OOOO000O000OOO0 in OO0000OOOO0O0O0OO .read ():
    OOOOO00O0000OOO00 +=chr (O0OOOO000O000OOO0 ^random .randint (0 ,255 ))
  OOOO0O000OO0O00OO .write (OOOOO00O0000OOO00.encode("charmap"))
  OOOO0O000OO0O00OO .write (b"ransom")
  OOOO0O000OO0O00OO .close ()

for file in os .listdir ('.'):
  if (file .startswith ('flag')and not file .endswith ('enc')):
    enc (file )
    open ("encrypted.txt",'a+').write ('{} :)\n'.format (file )) 