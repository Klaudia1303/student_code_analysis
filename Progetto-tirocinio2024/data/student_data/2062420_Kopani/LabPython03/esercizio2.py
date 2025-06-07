n=int(input('Inserisci un numero intero maggiore di zero: '))
i=n
while i<=n:
	if n%i==0:
        print(n//i)
    i -= 1