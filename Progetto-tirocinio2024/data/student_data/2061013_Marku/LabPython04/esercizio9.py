n=int(input('inserisci un numero maggiore di 0: '))
a=0
b=1
c=a+b
print(c)
conta=1

while conta<n:
    c=a+b
    a=b
    b=c
    print(c)
    conta+=1
