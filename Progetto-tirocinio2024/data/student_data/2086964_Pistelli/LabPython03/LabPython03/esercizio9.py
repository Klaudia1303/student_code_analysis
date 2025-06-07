a=True
while a:
    b=int(input('inserisi un numero '))
    if b%2==0 or b%3==0 or b%5==0:
        print('il numero non è primo')
    elif b%b==0 and b%1==0:
        print('il numero è primo')
        a=False
              
