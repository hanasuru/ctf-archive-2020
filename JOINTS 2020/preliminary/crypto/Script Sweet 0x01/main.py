#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
import os
import sys
from secret import koentji, rahasia

class AING_MAUNG_1337(object):
  def __init__(self, AES_KEY):
    self.aes_key = AES_KEY

  def encrypt(self, msg):
    msg   = self.pad(msg)
    iv    = os.urandom(16)
    msg   = [msg[i:i+16] for i in range(0, len(msg), +16)]
    prop  = iv
    ret_cipher = b''

    for i in range(len(msg)):
      enc   = self.enc_cbc(msg[i], prop)
      ret_cipher += enc
      prop  = strxor(msg[i], enc)

    return iv + ret_cipher

  def decrypt(self, cipher):
    iv      = cipher[:16]
    cipher  = [cipher[i:i+16] for i in range(16, len(cipher), +16)]
    prop    = iv
    ret_msg = b''

    for i in range(len(cipher)):
      dec   = self.dec_cbc(cipher[i], prop)
      ret_msg += dec
      prop  = strxor(cipher[i], dec)

    if self.cek_and_ricek(ret_msg):
      return self.unpad(ret_msg)
    else:
      return None

  def enc_cbc(self, input_block_msg, iv):
    obj = AES.new(self.aes_key, AES.MODE_CBC, iv)
    return obj.encrypt(input_block_msg)

  def dec_cbc(self, input_block_cipher, iv):
    obj = AES.new(self.aes_key, AES.MODE_CBC, iv)
    return obj.decrypt(input_block_cipher)

  def cek_and_ricek(self, cipher):
    if cipher[-1] <= 16 and len(cipher) % 16 == 0 and len(cipher) >= 16 :
      yo = chr(cipher[-1]) * cipher[-1]
      if cipher[-(cipher[-1]):] == yo.encode("latin-1"):
        return True
      else:
        return False
    return False

  def pad(self, msg):
    byte = 16 - len(msg) % 16
    return msg + (chr(byte) * byte).encode("utf-8")

  def unpad(self, msg):
    return msg[:-msg[-1]]


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

sys.stdout = Unbuffered(sys.stdout)


if __name__ == "__main__":
  aing_maung_1337 = AING_MAUNG_1337(koentji)
  cois = """1.) Send raw message
2.) Validate encrypted message
  """
  print("$$$ We are truly leet 'aing maung 1337' agent $$$")
  print("$$$ We will encrypt your message for safety $$$")
  print("$$$ Or you can validate your encrypted message to us $$$")

  while 0x01:
    print(cois)
    choice = input("Choice : ")

    if choice == "1":
      raw_msg = input("Your message : ")
      code_msg = rahasia + b"|1337|" + raw_msg.encode("latin")
      safe_msg = aing_maung_1337.encrypt(code_msg)
      print("Safe message : %s" % safe_msg.hex())
    elif choice == "2":
      safe_msg = input("Safe message (in hex) : ")
      try:
        safe_msg = bytes.fromhex(safe_msg)
        check_msg = aing_maung_1337.decrypt(safe_msg)
        if check_msg != None:
          print("Valid slurrrr")
        else:
          print("Error slurrrr")
      except:
        print("Error slurrrr")
    else:
      print("Invalid choice")
    print("\n")
    
  
