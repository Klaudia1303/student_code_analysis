i=0
l=0
while i==0:
    n=input("inserisci un numero (inserisci * per terminare) : ")
    if n!="*":
        if int(n)<0:
            l+=int(n)
    else:
        i=1
print(l)        
