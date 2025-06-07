termina=False
p=0
while not termina:
    n=input("immetti un intero (* per terminare): ")
    if n!="*":
        n=int(n)
        if n > 0:
            p+=1
    else:
        termina=True
        
print(p)   
