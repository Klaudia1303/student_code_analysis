n= int(input('inserisci un intero maggiore di 0: '))
x=1
y=1
print(x)
print(y)
for i in range (1,n-1):
    z=x+y
    x=y
    y=z
    print(z)
