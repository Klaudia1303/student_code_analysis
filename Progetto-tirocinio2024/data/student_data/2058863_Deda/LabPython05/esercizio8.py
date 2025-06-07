n=int(input('Inserisci intero dispari >=3 '))
y=0
for i in range(n//2+1):
    x=n//2-i
    print(' '*x+'*'*(y+1))
    y+=2
