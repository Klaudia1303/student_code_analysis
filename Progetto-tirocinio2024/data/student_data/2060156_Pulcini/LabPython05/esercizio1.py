s1=input('inserire una stringa:')
s2=input('inserire una stringa:')
i=0
j=0
if len(s1)==len(s2):
    while i<len(s1) and j<len(s2):
        print(s1[i],s2[j],sep='',end='')
        i+=1
        j+=1
else:
    print('le stringhe non hanno la stessa lunghezza')
