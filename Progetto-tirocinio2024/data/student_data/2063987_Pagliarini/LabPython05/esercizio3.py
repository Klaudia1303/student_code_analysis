s1=input('inserisci stringa ')
s2=input('inserisci stringa ')
y=0
for i in range(len(s1)):
    for x in range(len(s2)):
        if s1[i]==s2[x]:
            y=1
    if y==0:
         print(s1[i],end='')
    y=0
            
            
