n = int(input("inserisci la base di un triangolo (maggiore di 3): "))
spazio =(n//2)
for i in range(n+1):
    if i%2 != 0:
        print(" "*spazio, "*" * i," " * spazio)
        spazio -= 1
   
