n=int(input("Inserisci base triangolo isoscele: "))
for i in range(1,n+1,2):
    print((" ")*((n-i)//2)+("*"*i)+(" ")*((n-i)//2))
