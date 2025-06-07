s=input('inserire stringa contenente almeno due caratteri: ')
n=int(input('inserire n>0: '))
corretto=False
i=0
while i<len(s)-n:
    if s[i]==s[i+n]:
        corretto=True
    i+=1
print(corretto)

    
