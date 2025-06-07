n=int(input("Inserie un numero intero:"))
b=True
i=2
while i<n and b:
    if n%i==0:
        b=False
    else:
        i=i+1
if b:
    print("numero primo")
else:
    print("numero non primo")
    
