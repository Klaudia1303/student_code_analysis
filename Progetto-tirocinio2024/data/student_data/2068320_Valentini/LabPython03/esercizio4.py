n1=-1
n2=-1
while n1<0 or n1>10:
    n1=int(input("Inserire il primo numero: "))
while n2<0 or n2>10:
    n2=int(input("Inserire il secondo numero: "))
i=0
while i<11:
    if i!=n1 and i!=n2:
        print(i)
    i=i+1
