a = int(input('inserisci un intero: '))
i = 1
b = 0
while i<=a:
    if a%i==0:
        b += 1
    i +=1
if b == 2:
    print('numero primo')
else:
    print('numero non primo')

       
