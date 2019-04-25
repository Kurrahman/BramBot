question = open("source\\ask_data.txt","r")
answer = open("source\\ans.txt","r")
stopword = open("source\\stopword.txt","r")
synonimfile = open("source\\synonim.txt","r")
realquestion = open("source\\ask.txt","r")
pertanyaan = []
jawaban = []
sw = []
synonim = []
realq = []
for s in stopword:
	sw.append(s.rstrip())
for s in question:
	pertanyaan.append(s.rstrip())
for s in answer:
	jawaban.append(s.rstrip())
for s in synonimfile:
	synonim.append(s.rstrip())
for s in realquestion:
	realq.append(s.rstrip())

def cekChar(qtemp,c,j):
	jtemp = j
	j -= 1

	#kondisi 1
	while(j>=0):
		if(qtemp[j] == c):
			return (jtemp -j)
		else :
			j -= 1
	j = jtemp
	#kondisi 2		
	while(j<len(qtemp)-1):
		if(qtemp[j] == c):
			return 1
		else :
			j+= 1

	#kondisi 3
	return len(qtemp)		
			

def boyermoore(pattern,text):
	m = len(text) # panjang pertanyaan	
	n = len(pattern)
	i = n - 1
	j = n - 1
	ipointer = i
	while (i < m):
		if(pattern[j] == text[ipointer]):
			if (j == 0):
				return True
			else :
				ipointer -= 1
				j -= 1
		else :
			i += cekChar(pattern,text[ipointer],j)
			ipointer = i
			j = n - 1
	return False		

def bmsearch(qtemp,s):
	total = 0
	conf = 0
	for q in qtemp:
		total += len(q)
		if(boyermoore(q,s)):
			conf += len(q)
		else :
			#print("stuck")
			for sy in synonim:
				if(boyermoore(q,sy)):
					word = sy.split()
					#print(word)
					for w in word:
						#print(w)
						if(boyermoore(w,s)):

							conf += len(q)
							break
					break
	return (conf/total)*100	




def bm(query):
	

	query = query.replace("?","")
	query = query.replace("!","")
	query = query.replace(".","")
	query = query.replace(",","")
	query = query.split()
	qtemp = query.copy()

	for q in (query):
		# print(q)
		for s in (sw):
			if(q == s):
				qtemp.remove(q)
				break
	#print(qtemp)
	confindence = 0
	#tupel (index,confidence)
	confindenceMax = (-1,-1)
	c = 0
	#found = False
	# array tuple (index,confindence)
	suggestion = [(-1,-1),(-1,-1),(-1,-1)]

	for s in pertanyaan:	
		#print(s)			
		confindence = bmsearch(qtemp,s)
		if(confindence > confindenceMax[1]):
			confindenceMax = (c,confindence)

		for i in range(3):
			if(suggestion[i][1] < confindence):
				suggestion[i] = (c,confindence)
				break
		c += 1


	if (confindenceMax[1] >= 90):
		print (jawaban[confindenceMax[0]])
		print (';' + str(confindenceMax[1]))
	else :
		print("Pertanyaan Anda tidak memenuhi confident level yang telah ditentukan")
		print("Terdapat beberapa sugesti pertanyaan yang mungkin")
		c = 0
		for s in suggestion:
			if(s[1] >= 0):
				print (str(c)+".", realq[s[0]])
				c += 1
		print("Tuliskan kembali pertanyaan yang menurut Anda paling cocok")		