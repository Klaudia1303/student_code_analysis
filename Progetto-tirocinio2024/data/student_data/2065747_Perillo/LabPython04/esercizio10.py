s=input()
a=s
b=a
while len(s)!=len(a)+len(b):
    b=a
    a=s
    s=input()
print(a,b,s)
    
