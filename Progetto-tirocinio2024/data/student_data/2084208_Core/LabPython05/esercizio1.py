s1=input('Inserire una stringa: ')
s2=input('Inserire una stringa della stessa lunghezza della precedente: ')
for i in range (0,len(s1)):
    print(s1[i]+s2[i],end='')
