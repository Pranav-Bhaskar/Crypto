import sys
import os

options = """		Menu
	1. Encode using base64
	2. Encode using ShiftCypher
	3. Decode using base64
	4. Decode using ShiftCypher
	Any other NUMBER to EXIT
	"""
num2b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def GetFileName():
	try:
		ifPath = str(raw_input('Enter File Name : ').strip())
	except NameError:
		ifPath = str(input('Enter File Name : ').strip())
	if os.path.isfile(ifPath):
		return ifPath
	else:
		print('File "'+ ifPath + '" Doesnot Exists')
		return None


def E64():
	ifName = GetFileName()
	if ifName:
		f = open(ifName, 'rb').read()
		bytes = []
		for x in f:
			bytes.append(bin(x)[2:].zfill(8))
		bytes = ''.join(bytes)
		if len(bytes) % 3 == 1:
			bytes += '00'
			pad = '='
		elif len(bytes) % 3 == 2:
			bytes += '0'
			pad = '=='
		encoded = []
		for x in range(0, len(bytes), 6):
			oneSec = int(bytes[x:x+6], 2)
			encoded.append(num2b64[oneSec])
		encoded = ''.join(encoded)
		encoded += pad
		ofPath, ofName = os.path.split(ifName)
		ofName += '.b64'
		with open(ofName, 'w') as f:
			f.write(encoded)
		print('File Saved As ' + ofName)

def menu():
	print(options)
	try:
		opt = int(raw_input('Enter option : ').strip())
	except NameError:
		opt = int(input('Enter option : ').strip())
	except ValueError:
		print('Try Entering NUMBERS for a change')
		return True
	if opt == 1:
		E64()
		return True
	elif opt == 2:
		Esc()
		return True
	elif opt == 3:
		D64()
		return True
	elif opt == 4:
		Dsc()
		return True
	return False

if __name__ == '__main__':
	try:
		while True:
			if not menu():
				break
	except KeyboardInterrupt:
		sys.stdout.write('\nForce ')
		sys.stdout.flush()
	print('Exitting...')
	sys.exit(0)
