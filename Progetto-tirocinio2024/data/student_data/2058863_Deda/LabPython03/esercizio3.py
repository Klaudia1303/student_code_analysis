n=1
corretto=False
while not corretto:
    if  (n%5)>0 or (n%5)<0:
        n=int(input("Inserisci un intero "))
        print(n//5)
        corretto=False
    else:
        corretto=True
