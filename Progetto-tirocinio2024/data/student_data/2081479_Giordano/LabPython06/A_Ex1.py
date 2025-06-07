n1=int(input('insert a number: '))
n2=int(input('insert a number: '))
n1Div=False
n2Div=False

if n1<n2:
    startNumber=n2
    n2=n1
    n1=startNumber
else:
    startNumber=n1
for divisor in range(startNumber,1,-1):
    if n1%divisor==0:
        n1Div=True
    if n2%divisor==0:
        n2Div=True
    if n1Div==True and n2Div==False:
        print(divisor)
    n1Div=False
    n2Div=False