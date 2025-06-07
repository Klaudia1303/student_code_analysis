n="2"
count=0
while n!="*":
    n=input("inserisci numero intero, * per terminare")
    if n=="*":
        count=count
    elif  int(n)>0:
        count=count+1
       
print(count)
