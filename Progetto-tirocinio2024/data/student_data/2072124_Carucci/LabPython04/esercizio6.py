print('Inserire due numeri interi:')
x = int(input(' x = '))
y = int(input(' y = '))

p = 0

if y>0:
    while y>0:
        p+=x
        y-=1
else:
    while y<0:
        p-=x
        y+=1
    
print(p)
