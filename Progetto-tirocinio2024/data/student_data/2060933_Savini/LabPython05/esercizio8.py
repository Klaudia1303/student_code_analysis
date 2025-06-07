n= int(input('inserisci un intero dispari maggiore o uguale a 3: '))
for l in range(n+1):
    if l%2!=0:
        print(' '*((n-l)//2),'*' *l)
    
      
