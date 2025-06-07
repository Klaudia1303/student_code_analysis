b=int(input("Inserisci base del triangolo dispari maggiore o pari a 3: "))
for i in range(1,b+1,2):
    print(' '*((b-i)//2)+'*'*i)
