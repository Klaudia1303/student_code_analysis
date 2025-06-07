n1=int(input("Inserire il primo numero: "))
n2=int(input("Inserire il seconod numero: "))
for i in range(n1,1,-1):
    if n1%i==0 and  n2%i!=0: print(i)
