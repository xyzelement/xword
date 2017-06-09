import re

def getword(line):
   return line.split("\t")[1]; 

with open("clues.txt") as f:
    words = map(getword, f)


def getWordsByLen(length):
    def isLen(x):
        return len(x) == length
    return filter(isLen, words)

def matchPattern(pattern):
    print "A"
#print getWordsByLen(6);

print re.match("^333$","333")

