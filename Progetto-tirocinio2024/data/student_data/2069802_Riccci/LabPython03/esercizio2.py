n = int(input("Inserisci numero maggiore di 0 --> "))
while(n<=0):
    n = int(input("Input sbagliato, Inserisci numero maggiore di 0 --> "))
print(int("1"))
for i in range(2,int(n/2)+1):
    if n%i==0:
        print(i)
print(n)
