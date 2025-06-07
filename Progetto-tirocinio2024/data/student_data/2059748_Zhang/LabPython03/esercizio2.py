n=int(input("inserire un intero maggiore di zero: "))
x=int(1)
while n>0:
    if n//x>0 and n%x==0:
        print(x)
    x=x+1
