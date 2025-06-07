n=input('inserire un intero   ')
while not n.isnumeric :
    n=input('inserire un intero   ')
p=1
c=int(n)
while c!=0:
    p*=c
    c-=1
print('il fattoriale di',n,'è :',p)
