s=input('inserire una stringa')
n=int(input('inserire il numero di ripetizione di ogni singolo carattere: '))
for i in s:
    print(i*n, end='')
