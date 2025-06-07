s1=input('inserire una stringa: ')
i=0
s2=input('inserire una stringa di eguale numero di caraatteri rispetto la precedente:')
while i<len(s1):
    print(s1[i]+s2[i],end='')
    i+=1
