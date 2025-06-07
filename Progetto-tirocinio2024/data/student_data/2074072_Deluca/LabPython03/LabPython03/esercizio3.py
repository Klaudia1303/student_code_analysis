N=2
corretto=False
while not corretto:
    N=int(input("inserisci un numero"))
    if N%5==0:
        print(N/5)
        corretto=True
