s1=str(input('Inserisci stringa 1 '))
s2=str(input('Inserisci stringa 2 '))
u=0
c=0
a=''
for i in range(len(s1)):
    for j in range(len(s1)):
        y=s2.count(s1[i:j+1])
        z=len(s1[i:j+1])
        if y>=1 and z>u:
            a=s1[i:j+1]
            c=y
            u=z
    if c>(len(s1)//2+1):
        break
print(a)
