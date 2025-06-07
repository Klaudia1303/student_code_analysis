s1=input('Inseerire una stringa: ')
s2=input('Inseerire una seconda stringa della stessa lunghezza della prima: ')
i=0
f=''
for i in range(0,len(s1)):
     f+=s1[i:i+1]+s2[i:i+1]
print(f)
