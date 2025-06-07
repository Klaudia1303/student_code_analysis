x=0
y=0
while x!="*":
    x=input("inserire numero: ")
    if x!="*":
        if int(x)<0:
            y=y+int(x)
if x=="*":
    print(y)
