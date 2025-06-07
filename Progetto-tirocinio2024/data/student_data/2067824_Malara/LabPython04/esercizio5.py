n=int(input('inserire numero intero >= 0 ' ))
a=1
fattoriale=n
if n==0:
    print('1')
else:
    while a<n:
            fattoriale=fattoriale*a
            a+=1
    print(fattoriale)
