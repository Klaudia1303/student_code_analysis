a=int(input("inserire un numero primo "))
b=1
c=str(a)
while b<a:
    if a%b==0:
        c=c,str(b)
    
    
    b=b+1
if c==(str(a), '1'):
    print("numero primo")
else:
    print("numero non primo")
