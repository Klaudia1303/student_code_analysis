n=int(input("Inserisci numero che rappresenti lato quadrato --> "))
print("*"*n)
for i in range(n-2):
    print("*"*(int(n/2))+" "+"*"*(int(n/2)))
print("*"*n)
