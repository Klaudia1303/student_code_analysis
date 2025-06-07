n=int(input("inserire un numero intero (inserire 0 per terminare): "))
r=0
while n!=0:
    if n%3==0:
        r=r+n
    n=int(input("inserire un numero intero (inserire 0 per terminare): "))
print(r)
