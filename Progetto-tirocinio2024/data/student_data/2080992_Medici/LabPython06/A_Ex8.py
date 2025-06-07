s1=str(input('inserire una stringa: '))
s2=str(input('inserire una stringa: '))
n=int(input('inserire un numero: '))
s=''
for i in range(len(s1)):
    a=i+n
    b=i-n
    if b<0:
        b=0
    if a>len(s2):
        a=len(s2)-1
    for j in range(b,a):
        if s1[i]==s2[j]:
            s+=s1[i]
print(s)
