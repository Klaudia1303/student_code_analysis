s1=input('inserire una stringa:')
s2=input('inserire una stringa:')
n=int(input('inserire un numero intero:'))
s=''
for i in range(len(s1)):
    if s1[i] in s2 and abs((s2.find(s1[i]))-i)<=n:
        s+=s1[i]
print(s)
