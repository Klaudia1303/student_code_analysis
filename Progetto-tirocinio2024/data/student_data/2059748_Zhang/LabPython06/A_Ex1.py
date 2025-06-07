n1=int(input("scrivi un numero >0 : "))
n2=int(input("scrivi un numero >0 : "))

for i in range (n1+1,-1,-1):
    if i==0:
        continue
    if n1%i==0 and n2%i!=0:
        print(i)
    else:
        ""
