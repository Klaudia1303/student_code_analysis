n=int(input("inserire un numero (0 per terminare):"))
s=0
while n!=0:
    if n%3==0:
        s+=n
    n=int(input("inserire un numero (0 per terminare):"))
print("Somma dei numeri divisibili per 3=",s)
