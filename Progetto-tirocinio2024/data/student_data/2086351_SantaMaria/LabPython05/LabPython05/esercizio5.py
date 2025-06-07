s=input('Inserire una stringa di almeno due caratteri: ')
n=int(input('Inserire un intero positivo: '))
x=False
i=0
while i<(len(s)-n) and x==0:
    if s[i]==s[i+n]:
        x=True
    i+=1
print(x)
