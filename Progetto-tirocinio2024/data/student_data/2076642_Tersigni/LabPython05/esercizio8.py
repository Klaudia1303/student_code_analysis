n=int(input("inserisci la base di un triangolo isocele(numero dispari)"))
for i in range (n+1):
    if i%2!=0:
        print(((n-i)//2)* " ","*"*i)
