#!/usr/bin/env python

import string
from Crypto.Cipher import AES
import random
from pwn import *


class Exploit(object):
  def __init__(self, ip, port):
    self.IP = ip
    self.PORT = port
    self.conn = remote(self.IP, self.PORT)
    self.recovered_plaintext = list()
    self.BLOCK_SIZE = 16
    self.list_string = string.ascii_letters + string.digits

  def set_original_safe_msg(self, safe_msg):
    # pecah setiap blok
    self.original_safe_msg = list()
    for i in range(0, len(safe_msg), self.BLOCK_SIZE):
      self.original_safe_msg.append(safe_msg[i:i+self.BLOCK_SIZE])

    return True

  
  def get_initial_safe_msg(self):
    self.conn.sendlineafter("Choice : ", "1")
    self.conn.sendlineafter("message : ", "A")
    orig_safe_msg = self.conn.recvline().split(": ")[1][:-1]
    print orig_safe_msg
    self.set_original_safe_msg(orig_safe_msg.decode("hex"))

  def find_per_char(self, random_sequence, padded_sequence, target_block, byte_pad):
    for brute_byte in map(chr, range(0x100)):
      payload = random_sequence + brute_byte + padded_sequence + target_block
      payload = payload.encode("hex")
      self.conn.sendlineafter("Choice : ", "2")
      self.conn.sendlineafter("(in hex) : ", payload)
      hasil = self.conn.recvuntil("slurrrr")

      if "Valid slurrrr" in hasil:
        tmp_chr_intermediate = chr(ord(brute_byte) ^ (byte_pad))
        return tmp_chr_intermediate

    return False

  def find_per_block(self, target_block, previous_block=None):
    intermediate_per_block = ""

    for char_index in range(self.BLOCK_SIZE):
      random_sequence = self.generate_random_string(self.BLOCK_SIZE-char_index-1)
      padded_sequence = self.xor_string(intermediate_per_block, chr(char_index+1))
      char_intermediate = None
      # make while loop in case there is not found a invalid pad error in the brute force
      while not char_intermediate:
        char_intermediate = self.find_per_char(random_sequence, padded_sequence, target_block, char_index+1 )
      intermediate_per_block = char_intermediate + intermediate_per_block
    
    if previous_block:
      plain_block = self.xor_string(previous_block, intermediate_per_block)
      return intermediate_per_block, plain_block
    else:
      return intermediate_per_block


  def recover_plaintext(self):
    for block_index in range(len(self.original_safe_msg)-1):
      print block_index
      target_block = self.original_safe_msg[block_index+1]

      if block_index == 0:
        previous_block = self.original_safe_msg[block_index]
      else:
        previous_block = self.xor_string(self.recovered_plaintext[block_index-1], self.original_safe_msg[block_index])
      
      intermediate_per_block, tmp_plain = self.find_per_block(target_block, previous_block)
      self.recovered_plaintext.append(tmp_plain)
      print(self.recovered_plaintext)

    return self.recovered_plaintext


  def xor_string(self, str_a, str_b):
    xored_str = ""
    for i in range(len(str_a)):
      xored_str += chr(ord(str_a[i]) ^ ord(str_b[i % len(str_b)]))
    
    return xored_str

  
  def generate_random_string(self, len_str):
    random_string = ""
    for i in range(len_str):
      random_string += random.choice(self.list_string)
    
    return random_string


exploit_object = Exploit("localhost", 9998)
exploit_object.get_initial_safe_msg()
exploit_object.recover_plaintext()
print "".join(exploit_object.recovered_plaintext)

