n=int(input("assegna un numero intero dispari all lunghezza della base di un triangolo isoscele: "))

for i in range(n+1):
    if i%2!=0:
        print(((n-i)//2)*' ','*'*i)
