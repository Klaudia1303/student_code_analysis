n=int(input("Immetti un intero: "))
i=2
d=0
while i<n and d==0:
    if n%i==0:
        d+=1
    i+=1
if d==0:
    print("numero primo")
else:
    print("numero non primo")
