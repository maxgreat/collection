import sys
import glob
import os.path as path

if len(sys.argv) < 3:
	print("Usage : createList.py directory file")
	sys.exit(1)

with open(sys.argv[2], 'w') as f:
	for file in glob.glob(path.join(sys.argv[1], '*.jpg')):
		if not 'wall' in file:
			line = path.basename(file).split("_")
			f.write(line[0]+'_'+line[1]+"|"+path.basename(file)+'\n')


