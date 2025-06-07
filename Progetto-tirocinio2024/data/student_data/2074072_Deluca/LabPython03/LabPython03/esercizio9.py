n=int(input("inserisci numero"))
d=1
corretto=False
if n==2:
    print("numero primo")
else:
    while not corretto:
        d+=1
        if n%d!=0 and n>=d and d!=1:
            print("numero primo")
            correttetto=True
        elif n%d==0 and n>d and d!=1:
            print("numero non primo")
            corretto=True
