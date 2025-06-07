x=input('Inserire un numero intero: ')
p=0
while x!='*':
	if int(x)>=0:
		p+=1
	x=input('Inserire un numero intero: ')
print(p)