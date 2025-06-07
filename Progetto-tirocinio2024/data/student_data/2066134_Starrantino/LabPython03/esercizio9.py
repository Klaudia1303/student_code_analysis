n = int(input('> '))

div = 2
while div <= n//2:
    if n % div == 0:
        print('numero non primo')
        break
    div += 1
else:
    print('numero primo')