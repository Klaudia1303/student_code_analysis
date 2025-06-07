i = 0
tot = 1

n = int(input("Inserisci un numero intero: "))

if n == 0 and n == 1:
   print("1")
else:
    while i <=n:
        tot*=(n-i)
        i = i+1
        if n == i:
            print(tot)
