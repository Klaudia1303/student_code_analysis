n=0
count_pos=0
while n!='*':
    n=input('inserire un intero: ')
    if n!='*':
        n=int(n)
        if n>0:
            count_pos+=1
    else:
        print(count_pos)
