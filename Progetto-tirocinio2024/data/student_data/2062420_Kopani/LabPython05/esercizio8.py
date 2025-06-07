n=int(input('Inserire un intero dispari maggiore o uguale a 3: '))
h=(n+1)//2
ast=1
spaz=h-1
for i in range(h):
	print((' '*spaz)+('*'*ast))
	spaz-=1
	ast+=2