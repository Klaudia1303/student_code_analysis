k=True
while k:
    n1=int(input('Intero 1 '))
    n2=int(input('Intero 2 '))
    if n1>0 and n2>0:
        k=False
    else:
        print('Numeri non maggiori da 0')
for i in range(max(n1,n2)+1,2,-1):
    if n1%i==0 and n2%i!=0:
        print(i)
