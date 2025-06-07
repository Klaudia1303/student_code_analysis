n=0
count_neg=0
while n!='*':
    n=input('inserire un intero: ')
    if n!='*':
        n=int(n)
        if n<0:
            count_neg+=n
    else:
        print(count_neg)
    
