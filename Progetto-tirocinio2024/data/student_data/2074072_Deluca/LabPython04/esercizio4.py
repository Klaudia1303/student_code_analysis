n=2
count=0
while n!=0:
    n=int(input("inserisci numero intero, 0 per terminare"))
    if n%3==0:
        count=count+n
print(count)
