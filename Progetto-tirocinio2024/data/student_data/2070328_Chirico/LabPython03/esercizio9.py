#Riconosci un numero primo o non primo

n = int(input('Scrivi un intero = '))
d = n
x = 0

while d >= 1:
    if n%d == 0:
        x = x+1
        d = d-1
    elif n%d != 0:
        d = d-1

if x == 2:
    print('numero primo')
else:
    print('numero non primo')
