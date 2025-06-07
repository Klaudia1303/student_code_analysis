s=str(input('inserire un numero: '))
n=int(input('inserire un numero: '))
vero=True
i=0
while (i+n)<len(s):
    if s[i]==s[i+n] and vero:
        print(vero)
        vero=False
    i+=1
if vero==True:
    print(False)
