n1=int(input('inserire un numero intero>0'))
n2=int(input('inserire un numero intero>0'))
i=n1
while i>0:
    if n1%i==0 and n2%i!=0:
        print(i)
    i-=1
    
