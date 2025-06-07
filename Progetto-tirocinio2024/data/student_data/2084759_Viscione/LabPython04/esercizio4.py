termina=False
s=0
while not termina:
    n=int(input("immetti un intero (0 per terminare): "))
    if n!=0:
        if n%3==0:
            s=s+n
    else:
        termina=True
        
print(s)   
