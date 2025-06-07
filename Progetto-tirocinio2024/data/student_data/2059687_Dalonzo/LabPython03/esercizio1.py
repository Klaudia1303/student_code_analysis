

num = int(input('Inserire un numero intero maggiore di 2: '))
n = 2
if(num > 2):
    while(n <= num):
        if(n % 2) == 0:
            print(n)
        n+=1
else:
    print('E\' stato inserito un numero minore o uguale a 2')