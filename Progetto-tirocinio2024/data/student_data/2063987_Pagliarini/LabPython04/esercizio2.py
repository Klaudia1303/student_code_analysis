n=input("inserisci n oppure * per terminare: ")
i=0
while n!="*":
    n=int(n)
    if n>0:
        i+=1
    n=input("inserisci n oppure * per terminare: ")
print(i)

        
