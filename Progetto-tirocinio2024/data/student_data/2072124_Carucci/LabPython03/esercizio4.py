print('Inserire due numeri interi compresi tra 0 e 10:')
x = int(input(' x='))
y = int(input(' y='))

i = 0
while i<=10:
    if (i!=x) and (i!=y):
        print(i)
    i+=1
