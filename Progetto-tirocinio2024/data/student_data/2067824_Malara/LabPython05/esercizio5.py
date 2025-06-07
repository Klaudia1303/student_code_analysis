s=input('inserire stringa di almeno due cartteri: ')
n=int(input('inserire intero: '))
c=0
g=True
while c<len(s)-n and g:
    if s[c]==s[c+n]:
        print(True)
        g=False
    c+=1
if g==True:
    print(False)
