n=int(input('Inserire un intero maggiore di 0: '))
n1=0
n2=0
somma=1
while n>0:
	print(somma)
	n1=n2
	n2=somma
	somma=n1+n2
	n-=1