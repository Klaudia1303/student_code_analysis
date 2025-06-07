n = int(input('inserire numero intero positivo'))
i = 1
c = 0
while i <= n:
    if n%i == 0:
        c += 1
    i += 1
if c == 2:
    print('Numero primo')
else:
    print('Non si tratta di un numero primo')
