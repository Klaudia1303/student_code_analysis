x=int(input('Inserire un numero intero: '))
somma=0
while x!=0:
	if x%3==0:
		somma=somma+x
	x=int(input('Inserire un numero intero: '))
print(somma)