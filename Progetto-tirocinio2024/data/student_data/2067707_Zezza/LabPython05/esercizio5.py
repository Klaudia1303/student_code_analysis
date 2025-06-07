s=input('stringa almeno due caratteri: ')
n=int(input('distanza: '))
k=2
i=0
while i!=(len(s)-n) and k!=5:
    if s[i]==s[i+n]:
        print(True)
        k=5
    i+=1
if k!=5:
    print(False)
    
