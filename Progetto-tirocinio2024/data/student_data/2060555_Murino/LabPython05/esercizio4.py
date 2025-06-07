n1=int(input('inserisci un intero: '))
n2=int(input('inserisci un intero: '))
for n in range(n2):
    n=n+n1
    if n%n1==0 and n<n2:
        print(n)
