#! /usr/bin/python
import sys, getopt, string, os, math
'''
Performs the Friedman Attack on a Vigenere cipher
'''
def shiftChar( str, shift): # function to peform c-shift on a string
	retstr = "" # return string...
	for i in range(0,len(str)):
		c = ord(str[i])
		c+=shift
		if (c > 122):
			c-=26
		retstr+=chr(c)
	return retstr

def chi( str ):# gets chi-square value of string compared to expected values of english language
	expected = [0.0816,0.0149,0.0278,0.0425,0.1270,0.0222,0.0201,0.0609,0.0696,0.0015,0.0077,0.0402,0.0240,0.0674,0.0750,0.0192,0.0009,0.0598,0.0632,0.0905,0.0275,0.0097,0.0236,0.0015,0.0197,0.0007]
	cfreq = [0.0]*26
	chiSum = 0.0
	for i in range (0,26):
		cfreq[i] = (str.count(string.ascii_lowercase[i])/41.0)
		chiSum +=(( cfreq[i] - expected[i] )*( cfreq[i] - expected[i] ))/expected[i]
	return chiSum
	
print "*** Analysis *** 
if (  len(sys.argv) < 2):
	print "Usage : chiAnalysis.py <cipherText.file> [keylength]\nDefault keylength is set to 36"
	exit()
if ( sys.argv[1] == '-h'):
	print "Usage : chiAnalysis.py <cipherText.file> [keylength]\nDefault keylength is set to 36"
	exit()

inputFile = open(sys.argv[1],"r")
cipherText = inputFile.read()
cipherText = cipherText.lower()
inputFile.close()
cleanText =""
for i in range(0,len(cipherText)): #clean the ciphertext for processing
	if ((ord(cipherText[i]) > 96) & (ord(cipherText[i]) < 123)):
		cleanText += cipherText[i]
cipherText = ""
cipherText = cleanText
length = len(cipherText)
colNo = 36
rowLen = 41
if (len(sys.argv) > 2):
	colNo = int(sys.argv[2])
rowLen = int(math.floor(length/colNo))
print "Using keylength ",colNo
#print rowLen

col = [""]*colNo # prep the columns
finalCol = [""]*colNo
coreShift = [""]*colNo
for m in range(0,rowLen): #
	for i in range(0,colNo):
		col[i] += cipherText[(m*colNo)+i]
#
for m in range(0,colNo): # for each column
	bestChi = 99999 # init tobad score
	for i in range(0,26): # for each row, c-shift the column
		tempCol = shiftChar(col[m],i)
		score = chi(tempCol)
		if (score < bestChi): # keep the best fit
			bestChi = score	
			coreShift[m] = i 
			finalCol[m] = tempCol
			
#retrieve shift adjusted output and print
output =""
for c in range(0,rowLen):
	for o in xrange(colNo):
		output += finalCol[o][(c%colNo)]
print output

