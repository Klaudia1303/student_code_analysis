n=input("inserisci n oppure * per terminare: ")
somma=0
while n!="*":
    n=int(n)
    if n<0:
       somma+=n 
    n=input("inserisci n oppure * per terminare: ")
print(somma)
