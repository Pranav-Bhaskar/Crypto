import sys
dir1 = sys.argv[1]
key = sys.argv[2]

def decrypto():
	f1 = open(dir1,'r')
	f2 = open(dir1 + '.decrypto','w')
	data = f1.read()
	f1.close()
	i = 0
	for x in data:
		f2.write(chr(ord(x) - ord(key[i%len(key)])))
		i += 1
	f2.close()

decrypto()
