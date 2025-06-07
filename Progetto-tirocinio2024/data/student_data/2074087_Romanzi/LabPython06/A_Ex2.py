s=str(input('Stringa '))
f=0
for i in range(((len(s)-1)//2)+1):
    if s[i]==s[len(s)-i-1]:
        f=f+1
    else:
        break
if f>=len(s)/2:
    print('Livello: ',len(s))
else:
    print('Livello: ',f)
