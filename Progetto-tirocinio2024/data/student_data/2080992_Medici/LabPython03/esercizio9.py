n=int(input('scrivi un numero intero: '))
i=1
while i!=0:
    if n%2==0 and n!=2 and n%3==0 and n!=3 and n%5==0 and n!=5 and n%7==0 and n!=7:
        print('il numero non è primo')
        i-=1
    else:
        print('il numero è primo')
        i-=1
