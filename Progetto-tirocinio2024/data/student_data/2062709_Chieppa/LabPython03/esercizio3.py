n=int(input('inserire numero intero= '))
while n%5!=0:
    print(n)
    n=int(input('inserire numero intero= '))
    if n%5==0:
        print(n//5)
