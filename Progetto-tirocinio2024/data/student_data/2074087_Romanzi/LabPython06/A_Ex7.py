k=True
while k:
    s1=str(input('Stringa 1 '))
    s2=str(input('Stringa 2 '))
    if len(s1)!=0 and len(s2)!=0:
        k=False
    else:
        print('Stringhe non valide')
c=0
r=0
f=0
t=0
o=0
d=''
if len(s1)<len(s2):
    d=s1
    s1=s2
    s2=d
    
for i in range(len(s1)):
    c=0
    f=s2.find(s1[i])
    if f!=-1:
        o=i
        for j in range(s2.find(s1[i]),len(s2)):
            if len(s1)==o:
                break
            elif s1[o]==s2[j]:
                c=c+1
                o=o+1
            if c>=r:
                r=c
                t=f
for m in range(t,t+r):
    print(s2[m], end='')
