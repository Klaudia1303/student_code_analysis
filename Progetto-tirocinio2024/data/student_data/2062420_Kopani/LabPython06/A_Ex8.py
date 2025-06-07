s1=input('Inserire stringa s1: ')
s2=input('Inserire stringa s2: ')
n=int(input('Inserire numero n: '))
s=''
for i in range(len(s1)):
    f=s2.find(s1[i])
    if f==-1:
        continue
    if f-i<=n and i-f<=n:
        s=str(s)+str(s1[i])
print(s)