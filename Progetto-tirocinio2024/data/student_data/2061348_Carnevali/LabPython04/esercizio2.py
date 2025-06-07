x=0
n=0
while x!="*":
    x=(input("inserire un numero: "))
    if x!="*":
        i=int(x)
    if i>0:
        n=n+1
if x=="*":
    print(n)
