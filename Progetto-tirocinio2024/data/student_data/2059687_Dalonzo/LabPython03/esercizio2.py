

num = int(input('Inserire un numero maggiore di 0: '))
n = 1
if(num > 0):
    while(n <= num):
        if(num % n == 0):
            print(n)
        n += 1
else:
    print('Numero inserito minore di 0')