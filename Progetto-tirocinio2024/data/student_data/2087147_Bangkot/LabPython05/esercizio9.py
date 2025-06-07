l=int(input())
for i in range(1):
    print("*"*l)
    if l==3:
        for j in range(l-2):
            print("*","*")
    elif l>3:
        for j in range(l-2):
            print("*"," "*(l-4),"*")
print("*"*l)
    
