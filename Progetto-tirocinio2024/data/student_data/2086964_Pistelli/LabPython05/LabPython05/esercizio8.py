n=int(input('inserire un numero intero '))
if n%2!=0 and n>=3:
    a=0
    m=(n//2)+1
    for i in range(m):
        print((m-i)*(' '),'*'*(a+i+1))
        a+=1
