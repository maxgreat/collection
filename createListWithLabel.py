import sys

if len(sys.argv) < 3:
	print("Usage : createListWithLabel.py listImageFile outputFile")
	sys.exit(1)

with open(sys.argv[1], 'r') as f:
	with open(sys.argv[2], 'w') as fout :
		for line in f:
			if not 'wall' in line:
				stage, idx = line.split('_')[0:2]
				fout.write(stage+'_'+idx+'|'+line)
		

