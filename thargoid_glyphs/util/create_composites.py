import os, re
from PIL import Image
from fnmatch import fnmatch

innerRingMax=9

def createComposite(source, dest,name):
	nameNoExt = os.path.splitext(name)[0];
	for innerIndex in range(1, (innerRingMax+1)): 
		#Refresh images so prior loops don't have artefacts
		core = Image.open(os.path.join(source,"core.png")) 
		outer = Image.open(os.path.join(source,name))
		inner = Image.open(os.path.join(source,str(innerIndex) + ".png"))
		core.paste(inner, (0, 0), inner)
		core.paste(outer, (0, 0), outer)
		core.save( os.path.join(dest, nameNoExt + "-" + str(innerIndex) + ".png"), "PNG" )

if __name__ == "__main__":
	parentDir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

	symbolDir = os.path.join(parentDir,"images","symbols")
	compositeDir = os.path.join(parentDir,"images","composite")

	print(symbolDir)

	for path, subdirs, files in os.walk(symbolDir):
	    for name in files:
	    	if re.match('[0-9][A-Z].png',name):
	    		createComposite(symbolDir,compositeDir,name)
	    		print(name)
