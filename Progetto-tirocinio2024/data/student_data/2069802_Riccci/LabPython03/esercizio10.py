n = int(input("Inserisci numero intero positivo maggiore di 1 --> "))
while(n<=1):
    n = int(input("Input non valido, Inserisci numero intero positivo maggiore di 1--> "))
print(int("2"))
count=0
for i in range(3,n+1):
    j=2
    while(j<int(i/2)+1):
        if i%j==0:
            count+=1
        j+=1
    if(count==0):
        print(i)
