import re
import numpy as np

def loadWords():
	def getword(line):
   		return line.split("\t")[1]; 

	with open("clues.txt") as f:	
		return list(map(getword, f))


def loadShape():	
	with open("shape.txt") as f:
		carr = np.zeros((30,30), 'U1')
		row = 0
		for line in f:
			col = 0
			for c in line.rstrip():
				carr[row,col]=c
				col = col+1
				print(row,col,c)
			#print(line.rstrip())
			row=row+1
			print("ddd")
		print(carr)

#words = loadWords()
#print("Loaded Words: ", len(words))

loadShape()
