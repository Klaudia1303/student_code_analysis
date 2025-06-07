termina=False
s=0
while not termina:
    n=input("immetti un intero (* per terminare): ")
    if n!="*":
        n=int(n)
        if n < 0:
            s=s+n
    else:
        termina=True
        
print(s)   
