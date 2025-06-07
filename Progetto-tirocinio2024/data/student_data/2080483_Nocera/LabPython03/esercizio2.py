n = int(input("scrivi un intero maggiore di (0) :"))
l=1
while n>0:
    s= (n%l)
    if s==0 :
        print (int(l))
    l=l+1
    if l<=0:
        n=0
