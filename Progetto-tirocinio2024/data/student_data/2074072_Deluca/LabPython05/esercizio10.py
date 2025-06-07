n=int(input("lato: "))
print("*"*n)
for i in range(2,(n//2)+1):
    print("*"+" "*(i-2)+"*"+" "*(n-2*i)+"*"+" "*(i-2)+"*")
if n%2!=0:
    print("*"+(" "*((n-3)//2)+"*")*2)
for i in range((n//2),1,-1):
    print("*"+" "*(i-2)+"*"+" "*(n-2*i)+"*"+" "*(i-2)+"*")
print("*"*n)
