"""
tshark -r usb.pcapng -Y usb.capdata -Tfields -e usb.capdata > capdata
"""
capdata = map(lambda x: x.split(':')[2], open('capdata','r').read().split('\n')[:-1][::2])

key = {
	'28': 'ENTER',
	'4f': 'RIGHT',
	'51': 'DOWN',
	'50': 'LEFT',
	'52': 'UP'
}
seq = []
for i in capdata:
	seq.append(key[i])

print seq