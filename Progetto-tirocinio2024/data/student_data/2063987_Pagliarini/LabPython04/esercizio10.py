s=input('inserisci stringa: ')
s1=input('inserisci stringa: ')
c=0
while (len(s)+len(s1))!= c:
    if c==0:
        s2=input('inserisci stringa: ')
        c=len(s2)
    else:
        s=s1
        s1=s2
        s2=input('inserisci stringa: ')
        c=len(s2)
print(s,s1,s2)  
    
