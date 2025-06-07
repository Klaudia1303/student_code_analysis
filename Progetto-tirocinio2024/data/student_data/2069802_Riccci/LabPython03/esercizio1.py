n = int(input("Inserisci numero maggiore di 2 --> "))
while(n<=2):
    n =int(input("Input sbagliato , riprova (deve essere maggiore di 2) --> "))
for i in range(1,n+1):
    if i%2==0:
        print(i)
