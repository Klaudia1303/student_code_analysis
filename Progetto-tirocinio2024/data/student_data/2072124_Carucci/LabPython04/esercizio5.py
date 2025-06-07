n = int(input('Inserire un numero intreo maggiore o uguale a 0: '))

f=1

if n==1 or n==0:
    f=0

while n>1:
    f*=n
    n-=1

print(f)
