n=input("Inserisci numero (*) per terminare: ")
count=0
while n!='*':
    n=int(n)
    if n<0:
        count +=n
    n=input("Inserisci numero (*) per terminare: ")
print(count)
