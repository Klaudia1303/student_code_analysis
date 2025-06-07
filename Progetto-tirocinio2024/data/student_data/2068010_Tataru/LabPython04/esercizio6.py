a=int(input())
b=int(input())
p=0
if(a==0 or b==0):
    print("0")
elif(a<0 and b>0):
    for i in range(0,b):
        p+=a
    print(p)
elif(a>0 and b<0):
    for i in range(0,a):
        p+=b
    print(p)
else:
    for i in range(0,abs(a)):
        p+=abs(b)
    print(p)
