n=input("inserire un numero (* per terminare):")
s=0
while n!="*":
    n=int(n)
    if n<0:
        s+=n
    n=input("inserire un numero (* per terminare):")
print("Somma dei numeri negativi inseriti=",s)
