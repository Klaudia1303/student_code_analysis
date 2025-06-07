s=input('inserire una stringa da almeno due caratteri: ')
n=int(input('inserire un numero: '))
for i in range(0,len(s)-2):
    k=0
    if s[i]==s[i+n]:
        k=k+1
if k==0:
    print(False)
else:
    print(True)

