#!/usr/bin/python3

def normal():
	print('okay thanks uwu')

def winner():
	print('Congratz, here is your flag: ' + open('flag.txt').read())

real_return_address = 'normal'
my_input = input('Enter your name (max 32 characters)\n').ljust(32, '\x00')
my_input += real_return_address
return_address = my_input[32:32+6]
try:
	locals()[return_address]()
except:
	print('SIGSEGV')