ask = ["" for x in range(43)]
ans = ["" for x in range(43)]
daftar = ["" for x in range(43)]
synonim = ["" for x in range(27)]
stop = ["" for x in range(758)]

def readfile(array, namafile):
    f = open(namafile, "r")
    f1 = f.readlines()
    i = 0
    for x in f1:
        array[i] = x.rstrip()
        i += 1
        
def inputdatabase(ask, ans, stop):
    readfile(ask, "source\\ask_data.txt")
    readfile(ans, "source\\ans.txt")
    readfile(stop, "source\\stopword.txt")
    readfile(daftar, "source\\ask.txt")
    readfile(synonim, "source\\synonim.txt")
    
    
# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
    m = len(pat) 
    n = len(txt) 
  
    b = [0]*m 
    
    computerFail(pat, b, m) 
  
    i = 0 
    j = 0
    while i < n: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
        else:
        	if j!=0 :
        		j = b[j-1]
        	else:
        		i += 1
                
        if j == m: 
            return True
        j = b[j-1]
    return False
  
def computerFail(pat, b, m): 
    len = 0 
  
    b[0] = 0
    i = 1
    while i < m: 
        if pat[i]== pat[len]: 
            len += 1
            b[i] = len
            i += 1
        else: 
            if len != 0: 
                len = b[len-1] 
            else: 
                b[i] = 0
                i += 1


def kmp(pattern):
    inputdatabase(ask, ans, stop)
    pattern = pattern.translate({ord(i): None for i in '?!.,'}) #hapus tanda baca
    pattern = pattern.rstrip()
    pattern = pattern.lower()
    kata = pattern.split(" ")

    #hapus stopword dari input
    for x in kata[:]:
        if x in stop :
            kata.remove(x)
    #cari pertanyaan yang cocok     
    max1 = 0.0
    max2 = 0.0
    max3 = 0.0
    indeks1 = -1
    indeks2 = -1
    indeks3 = -1
    for x in ask:           
        le = len(x) - x.count(" ")
        bag = 0
        for y in kata:
            if(KMPSearch(y, x)):
                bag += len(y)
            else:
                for j in synonim:
                    word = j.split(" ")
                    if(KMPSearch(y, j)) and (KMPSearch(word[0], x)):
                        bag += len(word[0])

        #biar bisa ngasih sugestion
        if (bag/le) > max1:
            max3 = max2
            max2 = max1
            max1 = bag/le
            indeks1 = ask.index(x)
        elif (bag/le) > max2:
            max3 = max2
            max2 = bag/le
            indeks2 = ask.index(x)
        elif (bag/le) > max3:
            max3 = bag/le
            indeks3 = ask.index(x)
            
    if max1>0.9:
        print(str(int(max1*100)))
        print(ans[indeks1])
    else :
        print("Petanyaan Anda tidak memenuhi confident level yang telah ditentukan")
        print("Terdapat beberapa sugesti pertanyaan yang mungkin")
        if(indeks1 != -1):
            print("1. " + daftar[indeks1])
        if(indeks2 != -1):
            print("2. " + daftar[indeks2])
        if(indeks3 != -1):
            print("3. " + daftar[indeks3])
        print("Tuliskan kembali pertanyaan yang menurut Anda paling cocok")
        
