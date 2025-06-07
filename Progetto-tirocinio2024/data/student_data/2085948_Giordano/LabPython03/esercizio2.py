n=int(input("Inserisci un numero maggiore di 0: "))
print("I divisori del numero sono: ")
for num in range(1, n+1):
    if (n%num==0):
        print(num)
