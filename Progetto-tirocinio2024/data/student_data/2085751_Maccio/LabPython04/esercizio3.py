n=input("inserire intero: ")
sn=0
while n!="*":
    n=int(n)
    if n<0:
        sn=n+sn
    n=input("inserire intero: ")
print(sn)
