import sys

if len(sys.argv) < 3:
	print("Usage : ListImageFromFile.py fileWithImages output") 
	sys.exit(1)

with open(sys.argv[1], 'r') as f:
	with open(sys.argv[2], 'w') as fout :
		for line in f:
			s = line.split("_")
			fout.write(s[0]+'_'+s[1]+'|'+line)
