num=input('inserisci un numero maggiore strettamente di 2: ')
num=int(num)
while num>=2:
    if num%2==0:
        print(num)
    else:
        print('')

    num=num-1
