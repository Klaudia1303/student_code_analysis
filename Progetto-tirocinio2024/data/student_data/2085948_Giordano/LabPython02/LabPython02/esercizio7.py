n1=int(input("Inserire n1: "))
n2=int(input("Inserire n2: "))
n3=int(input("Inserire n3: "))
if (n1<n3 and n1<n2):
    if(n2<n3):
        print(n3)
        print(n2)
        print(n1)
         else:
         print(n2)
         print(n3)
         print(n1)
if(n2<n1 and n2<n3):
    if (n1<n3):
        print(n3)
        print(n1)
        print(n2)
        else:
        print(n1)
        print(n3)
        print(n2)
elif(n3<n1 and n3<n2):
    if(n1<n2):
        print(n2)
        print(n1)
        print(n3)
        if(n2<n1):
            print(n1)
            print(n2)
            print(n3)
