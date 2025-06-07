n1=int(input('Inserire due numeri interi: '))
n2=int(input('Inserire due numeri interi: '))
for k in range(n2):
	if k>=n1 and k%n1==0:
		print(k)