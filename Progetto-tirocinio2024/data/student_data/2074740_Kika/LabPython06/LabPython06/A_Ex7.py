s1=input('inserisci stringa: ')
s2=input('inserisci stringa: ')
c='a'
for i in range(len(s1)):
    for j in range(i+1,len(s1)):
        k=s1[i:j]
        b=s2.find(s1[i:j]) 
        if b!=-1 and len(k)>=len(c):
            c=k
        if b==-1:
            break
print(c)
