n1=int(input('inserire un numero: '))
n2=int(input('inserire un numero: '))
mn1=0
i=1
for i in range(1,n2):
    mn1=n1*i
    if mn1<n2:
        print(mn1)
    
