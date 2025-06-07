n=input("inserire un numero n: ")
neg = 0
while n!="*" :
    if int(n) < 0 :
        neg = neg +int(n)
        n=input("inserire un numero n: ")

print("La somma dei numeri negativi è "+str(neg))
