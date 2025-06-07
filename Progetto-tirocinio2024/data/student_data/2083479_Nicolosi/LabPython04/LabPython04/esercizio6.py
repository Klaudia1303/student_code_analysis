x=int(input('Inserisci un numero intero: '))
y=int(input('Inserisci un numero intero: '))
n=1
z=0
while n<=abs(y):
    z=z+x
    n+=1
if (y>0 and x>0) or (y<0 and x<0) or(y>0 and x<0):
    print(z)
elif (y<0 and x>0)  (y>0 and x<0):
    print(-z)