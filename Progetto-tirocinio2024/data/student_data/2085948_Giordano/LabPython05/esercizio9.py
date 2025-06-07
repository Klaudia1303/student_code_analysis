base = int(input("Inserisci la lunghezza del lato: "))

for i in range(base):
    for j in range(base):
        if i==0 or i==base-1 or j==0 or j==base-1:
            print("*",end="")
        else:
            print(" ",end="")
         
         
         
         
    print()