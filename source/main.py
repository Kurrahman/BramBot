import bm
import kmp
import regex
import sys
def main(x, quest):
	if(x==1):
		kmp.kmp(quest)
	elif(x==2):
		bm.bm(quest)
	elif(x==3):
		regex.regex(quest)
main(int(sys.argv[1]), sys.argv[2])
