x=input('Inserire un numero intero: ')
somma=0
while x!='*':
	if int(x)<0:
		somma=somma+int(x)
	x=input('Inserire un numero intero: ')
print(somma)