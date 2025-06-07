n = int(input('Inserire un intero n: '))
stringa = input('Inserire una stringa: ')

for i in range(0,len(stringa)):
    print(stringa[i] * n,end='')
