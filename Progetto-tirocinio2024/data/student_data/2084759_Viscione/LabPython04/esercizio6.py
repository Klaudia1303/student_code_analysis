n1=int(input("immetti primo intero:"))
n2=int(input("immetti secondo intero:"))
p=0
i=1
while i<=abs(n2):
    if n2>=0:
        p=p+n1
    else:
        p=p-n1
    i+=1
print(p)
