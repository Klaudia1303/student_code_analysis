x = int(input("Inserisci numero intero compreso tra 0 e 10 --> "))
y = int(input("Inserisci numero intero compreso tra 0 e 10 --> "))
if(x<=10 and x>=0 and y>=0 and y<=10):
    for i in range(0,11):
        if i!=x and i!=y:
            print(i)
else:
    print("Input sbagliato ")
