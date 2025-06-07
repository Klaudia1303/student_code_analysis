s1=input('inserire una stringa non vuota   ')
while len(s1)==0:
    s1=input('inserire una stringa non vuota   ')
s2=input('inserire una stringa non vuota   ')
while len(s2)==0:
    s2=input('inserire una stringa non vuota   ')
s=''
for i in range(len(s1)):
    c=0
    for j in range(len(s2)):
        if s1[i+c]==s2[j]:
            s+=s2[j]
        elif len(s)>0 or i+c+1>len(s1)-1:
            break
        c+=1
print(s)
