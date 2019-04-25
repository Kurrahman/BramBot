from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

factory = StemmerFactory()
stemmer = factory.create_stemmer()
question = open("source/ask_data.txt","r")
answer = open("source/ans.txt","r")
stopword = open("source/stopword.txt","r")
synonimfile = open("source/synonim.txt","r")
sw = []
pertanyaan = []
jawaban = []
synonim = []
for s in stopword:
	sw.append(s.rstrip())
for s in question:
	pertanyaan.append(s.rstrip())
for s in answer:
	jawaban.append(s.rstrip())
for s in synonimfile:
	synonim.append(s.rstrip())



def cekRegex(query,ask):
	kata = len(query)
	c = 0
	for q in query:
		if (re.search(r'%s' % (q), ask,re.IGNORECASE)):
			c += 1
		else :
			for sy in synonim:
				if (re.search(r'%s' % (q), sy,re.IGNORECASE)):
					word = sy.split()
					for w in word:
						
						if (re.search(r'%s' % (stemmer.stem(w)), ask,re.IGNORECASE)):
							c += 1
							break
					break
	return (c == kata)

def regex(query):
	query.replace("?","")
	query = stemmer.stem(query)
	query = query.split()
	qtemp = query.copy()

	for q in (query):
		# print(q)
		for s in (sw):
			if(q == s):
				qtemp.remove(q)
				break

	#print (qtemp)
	c = 0
	#print(pertanyaan)
	for s in pertanyaan:
		if (cekRegex(qtemp,stemmer.stem(s))):
			print(str(jawaban[c]) + ";100")
			return
		else :
			c += 1