n1=int(input('inserire primo intero >0:'))
n2=int(input('inserire secondo intero >0:'))
for i in range(n1,1,-1):
    if n1%i==0 and n2%i!=0:
        print(i)
