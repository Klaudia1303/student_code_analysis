s1=s2=''
while s1=='':
    s1=input('inserisci una stringa non vuota: ')
while s2=='':
    s2=input('inserisci un\'altra stringa non vuota: ')
stringa=''
mass=0
for i in range (len(s1)):
    if s2.count(s1[i])==0:
        continue
    else:
        for pos in range (len(s2)):
            sequenza=''
            num=0
            if s2[pos]==s1[i]:
                for j in range (min((len(s1)-i),(len(s2)-pos))):
                    if s1[i+j]==s2[pos+j]:
                        sequenza=sequenza+s1[i+j]
                        num+=1
                        if num>mass:
                            mass=num
                            stringa=sequenza
                    else:
                        break
print (stringa)
