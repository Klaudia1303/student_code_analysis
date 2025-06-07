a,b=map(int,input("Inserisci due numeri tra 0 e 10: ").split( ))
for num in range(0,10):
    if (num==a or num==b):
        continue
    print(num,end=" ")

