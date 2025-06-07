n= int(input('inserire un numero intero positivo "z" maggiore di 1:'))
while n>1:
    div,count=2,0
    while div<=n/2 and count==0:
        if n%div==0:
            count+=1
        div+=1
    if count==0:
        print(n)
    n-=1
    if n%div==0:
        count+=1
