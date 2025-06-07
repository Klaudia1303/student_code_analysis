s = input('Inserire una stringa: ')
n = int(input('Inserire un numero intero: '))

for i in range(len(s)):
    print(s[i]*n, end='')
