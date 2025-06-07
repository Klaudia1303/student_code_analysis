x=int(input('inserire numero intero: '))
a=True
while a:
    if x%5 != 0:
        x=int(input('inserire numero intero: '))
    else:
        print(int(x/5))
        a=False
