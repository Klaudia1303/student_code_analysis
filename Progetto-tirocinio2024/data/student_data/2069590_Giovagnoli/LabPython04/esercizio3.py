n = input("Inserire un numero intero (* per terminare): ")
somma=0
if n!="*":
    if int(n)<=0:
        somma = somma + int(n)
while n!="*":
    n=input("Inserire un numero intero (* per terminare): ")
    if n!="*":
        if int(n)<=0:
            somma = somma + int(n)
print("La somma è: ",somma)