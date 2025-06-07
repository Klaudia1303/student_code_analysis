x=int(input('inserire un intero   '))
y=int(input('inserire un intero   '))
c=y
p=0
if x==0 or y==0:
    c=0
while c!=0:
    p+=x
    c-=1
print('il loro prodotto è',p)
