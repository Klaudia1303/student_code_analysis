x=int(input('Inserire il primo intero: '))
y=int(input('Inserire il secondo intero: '))
y1=y
x1=x
p=0
if y==0 or x==0:
	print(0)
elif x>0 and y>0:
	while y1!=0:
		p=p+x
		y1-=1
	print(p)
elif x>0 and y<0:
	while y1!=0:
		p=p-x
		y1+=1
	print(p)
elif x<0 and y>0:
	while y1!=0:
		p=p+x
		y1-=1
	print(p)
elif x<0 and y<0:
		while y1!=0:
			p=p-x
			y1+=1
		print(p)