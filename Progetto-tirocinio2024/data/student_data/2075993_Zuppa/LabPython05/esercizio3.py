s1=input('inserire una stringa   ')
s2=input('inserire una stringa   ')
s=''
for i in range(len(s1)):
    if s1[i] not in s2:
        s+=s1[i]
print(s)
