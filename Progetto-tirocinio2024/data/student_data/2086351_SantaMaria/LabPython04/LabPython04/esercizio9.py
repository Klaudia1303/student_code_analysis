n=int(input('Inserisci un intero: '))
a=1
b=1
print(a)
if n>1:
    print(b)
    i=2
    while i<n:
        c=a+b
        a=b
        b=c
        i+=1
        print(c)
