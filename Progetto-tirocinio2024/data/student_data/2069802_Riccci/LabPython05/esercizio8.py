n=int(input("Inserisci numero che rappresenti base del triangolo (dispari) --> "))
for i in range(1,n,2):
    print(" "*(int((n-i)/2)),"*"*i," "*(int((n-i)/2)))
    
