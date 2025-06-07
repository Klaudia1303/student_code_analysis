n=int(input("Inserisci un numero intero"))
cond = False
fatt=1
if n==0 or n==1:
    print(1)
    cond = True
while not cond:
    while n>=1:
        fatt*=n
        n-=1
    if n<1:
        cond = True   
print(fatt)        
