s1=input('inserire una stringa   ')
s2=input('inserire una stringa della stessa lunghezza   ')
while len(s1)!=len(s2):
    print('le stringhe non hanno la stessa lunghezza')
    s1=input('inserire una stringa   ')
    s2=input('inserire una stringa della stessa lunghezza   ')
s=''
for i in range(len(s1)):
    s+=(s1[i]+s2[i])
print(s)
