N=int(input("inserisci numero positivo"))
D=0
corretto=False
while not corretto:
    D+=1
    if N%D==0:
        print(D)
    if N<D:
        corretto=True
