n=(input("inserisci un numero (* per terminare):"))
s=0
while n!="*":
    n=int(n)
    if n>0:
        s+=1
    n=(input("inserisci un numero (* per terminare):"))
print("sono stati inseriti",s,"numeri positivi")
