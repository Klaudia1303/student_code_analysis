n=int(input('inserire numero intero maggiore di 0: '))
a=n
while 0<a<=n:
    if n%a == 0:
        print(int(n/a))
        a=a-1
    else:
        a=a-1
