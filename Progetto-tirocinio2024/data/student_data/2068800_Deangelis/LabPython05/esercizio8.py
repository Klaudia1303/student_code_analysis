n = int(input("inserisci la base: "))
for i in range(n+1):
    if i%2!=0:
        print((' '*(n-i//2))+('*'*i))