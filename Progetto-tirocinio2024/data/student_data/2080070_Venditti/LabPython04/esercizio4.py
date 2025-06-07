n=0
count_divisibili=0
while n!='0':
    n=input('inserire un intero: ')
    if n!='0':
        n=int(n)
        if n%3==0:
            count_divisibili+=n
    else:
        print(count_divisibili)
