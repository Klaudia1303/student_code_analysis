n=input("Inserisci numero (*) per terminare: ")
count=0
while n!='*':
    n=int(n)
    if n>0:
        count +=1
    n=input("Inserisci numero (*) per terminare: ")
print(count)
