n1= int(input('numero1: '))
n2= int(input('numero2: '))
ris=0
x=1
for i in range(n2):
    ris= n1*x
    x= x+1
    if ris<n2:
        print(ris)
