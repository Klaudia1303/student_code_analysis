x=1
y=0
while x!=0:
    x=int(input("inserire numero: "))
    if x%3==0:
        y=y+x
if x==0:
    print(y)
