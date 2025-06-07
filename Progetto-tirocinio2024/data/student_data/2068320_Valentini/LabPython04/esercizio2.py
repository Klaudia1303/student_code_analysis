n=input("inserire un numero intero n: ")
intero = 0
while n!="*" :
    if int(n) > 0 :
        intero = intero + 1
    n=input("inserire un numero intero n: ")

print("Il numero di numeri interi positivi inseriti è "+str(intero))
