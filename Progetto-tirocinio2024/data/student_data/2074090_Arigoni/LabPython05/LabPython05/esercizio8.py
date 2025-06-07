n=int(input("Inserisci la base del triangolo>> "))
for i in range(1,n+1,2):
    print(' '*int(n+1),'*'*i,' '*int(n+1))
    n=n-1
