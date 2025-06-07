n= int(input('inserisci un intero >=0: '))
i=True
c=1
p=1
while i:
    if c<=n and n>=0:
        p=c*p
        c=c+1
    else:
        i=False
print(p)

    
