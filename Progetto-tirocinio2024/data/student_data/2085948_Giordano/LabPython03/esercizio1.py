n=int(input("Inserisci un numero maggiore di 2: "))
start,end=2, n
for num in range(start,end):
    if num % 2==0:
        print(num)
