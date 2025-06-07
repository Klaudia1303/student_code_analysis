n = int(input("Inserisci la base di un triangolo isoscele(n dispari): "))
for i in range(n+1):
    if i % 2  != 0 and n >=3:
        print((n-i//2)*' ',"*"*i)
