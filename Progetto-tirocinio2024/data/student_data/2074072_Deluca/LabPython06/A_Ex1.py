n1=int(input("inserisci numero: "))
n2=int(input("inserisci numero: "))
for i in range(n1+1,2,-1):
   if n1%i==0 and n2%i!=0:
       print(i)
       
       
