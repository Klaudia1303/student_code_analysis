n1=int(input('inserire intero >0: '))
n2=int(input('inserire intero >0: '))
for i in range(n1,0,-1):
       if n1%i==0 and n2%i!=0:
           print(i)
       
