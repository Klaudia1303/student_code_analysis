s1=input('inserisci stringa')
s2=input('inserisci stringa')
n=int(input('inserisci passo'))
p=''
for i in range (len(s1)):
    if s1[i] in s2:
        a=s1.find(s1[i])
        b=s2.find(s1[i])
        c=a-b
        if c<0:
            c=-c
        if c<=n:
            p+=s1[i]
    else:continue
print(p)

        
