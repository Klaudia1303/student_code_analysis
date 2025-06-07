n=input("inserire un numero intero (inserire * per terminare): ")
r=0
while n!="*":
    if n!="*":
        n=int(n)
        if n>0:
            r+=1
    n=input("inserire un numero intero (inserire * per terminare): ")
print(r)
