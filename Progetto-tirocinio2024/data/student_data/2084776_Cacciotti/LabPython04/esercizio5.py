n=int(input('inserire un numero'))
if n==0 or n==1:
    print(1)
fattoriale=1
while n>1:
    fattoriale=fattoriale*n
    n=n-1

print(fattoriale)
