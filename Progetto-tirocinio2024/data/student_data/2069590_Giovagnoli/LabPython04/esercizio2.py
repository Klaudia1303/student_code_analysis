n = input("Inserire un numero intero (* per terminare): ")
c=0
if n!="*":
    if int(n)>=0:
        c+=1
while n!="*":
    n=input("Inserire un numero intero (* per terminare): ")
    if n!="*":
        if int(n)>=0:
            c+=1
print("Ci sono ",c," numeri positivi!")