n1=int(input())
n2=int(input())
i=n1+n2
if n1>0 and n2>0:
   while (i>0):
      if n1%i==0 and n2%i!=0:
         print(i)
      i-=1
