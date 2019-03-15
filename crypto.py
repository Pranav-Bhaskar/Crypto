import sys
import os

options = """		Menu
	1. Encode using base64
	2. Encode using ShiftCypher
	3. Decode using base64
	4. Decode using ShiftCypher
	5. Encode/Decode using XOR
	Any other NUMBER to EXIT
	"""
num2b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

b642num = { x : i for x, i in zip(num2b64, range(0, len(num2b64)))}

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
		pad = ''
		if len(bytes) % 6 != 0:
			pad = '='*(len(bytes)%3)
			bytes += '0'*(6 - (len(bytes)%6))
		encoded = []
		for x in range(0, len(bytes), 6):
			oneSec = int(bytes[x:x+6], 2)
			encoded.append(num2b64[oneSec])
		encoded = ''.join(encoded)
		encoded += pad
		ofPath, ofName = os.path.split(ifName)
		ofName += '.b64'
		with open(os.path.join(ofPath, ofName), 'w') as f:
			f.write(encoded)
		print('File Saved As ' + ofName)

def D64():
	ifName = GetFileName()
	if ifName:
		f = open(ifName, 'r')
		base64 = f.readline().strip()
		f.close()
		pad = base64.count('=')
		if pad:
			base64 = base64[:-pad]
			pad = 3 - pad
		byte = [bin(b642num[x])[2:].zfill(6) for x in base64]
		byte = ''.join(byte)
		if pad:
			byte = byte[:-pad]
		data = []
		for x in range(0, len(byte), 8):
			data.append(int(byte[x:x+8], 2))
		ofPath, ofName = os.path.split(ifName)
		ofName += '.b64'
		with open(os.path.join(ofPath, ofName), 'wb') as f:
			f.write(bytes(data))
		print('File Saved As ' + ofName)

def Shc(sign):
	ifName = GetFileName()
	if ifName:
		try:
			key = int(input('Enter Key : '))
		except ValueError:
			print('Try Entering NUMBERS for a change')
			return
		data = ''
		with open(ifName, 'r') as f:
			for line in f:
				data += line
		enc = ''
		for x in data:
			if x.isdigit():
				x = chr(((ord(x) - ord('0')) + (sign*(key%10)))%10 + ord('0'))
			elif x.islower():
				x = chr(((ord(x) - ord('a')) + (sign*(key%26)))%26 + ord('a'))
			elif x.isupper():
				x = chr(((ord(x) - ord('A')) + (sign*(key%26)))%26 + ord('A'))
			enc += x
		ofPath, ofName = os.path.split(ifName)
		ofName += '.shc'
		with open(os.path.join(ofPath, ofName), 'w') as f:
			f.write(enc)
		print('File Saved As ' + ofName)

def Xor():
	ifName = GetFileName()
	if ifName:
		f = open(ifName, 'rb').read()
		byt = []
		for x in f:
			byt.append(bin(x)[2:].zfill(8))
		byt = ''.join(byt)
		pas = [bin(ord(x))[2:] for x in input('Enter Key : ').strip()]
		pas = ''.join(pas)
		encByte = []
		for x in range(len(byt)):
			encByte.append(str(int(byt[x])^int(pas[x%len(pas)])))
		encByte = ''.join(encByte)
		ofPath, ofName = os.path.split(ifName)
		ofName += '.xor'
		data = []
		for x in range(0, len(encByte), 8):
			data.append(int(encByte[x:x + 8], 2))
		with open(os.path.join(ofPath, ofName), 'wb') as f:
			f.write(bytes(data))
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
		Shc(+1)
		return True
	elif opt == 3:
		D64()
		return True
	elif opt == 4:
		Shc(-1)
		return True
	elif opt == 5:
		Xor()
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
