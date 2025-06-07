s1=input('Inserire una stringa: ')
s2=input('Inserire una seconda stringa: ')
lungstringa=0
strpiulunga=''
for i in range (len (s1)) :
    stringa=''
    for j in range (i,len(s1)):
        stringa+=s1[j]
        l=len(stringa)
        if s2.find(stringa)==-1:
            break
        elif l>=lungstringa:
                strpiulunga=stringa
                lungstringa=l
print (strpiulunga)
