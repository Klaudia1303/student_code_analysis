n=int(input("inserisci n: "))
i=0
while i<n:
    if i==0 or i==1:
        print(1)
        a=i
        b=i
    else:
        print( a+b )
        z=a+b
        a=b
        b=z
    i+=1
    
