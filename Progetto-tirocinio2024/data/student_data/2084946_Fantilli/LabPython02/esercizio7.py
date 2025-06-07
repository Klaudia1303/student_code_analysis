n1 = input()
n1 = int(n1)
n2 = input()
n2 = int(n2)
n3 = input()
n3 = int(n3)
if n1 > n2 > n3 :
    print(n1)
    print(n2)
    print(n3)
elif n1 > n3 > n2 :
    print(n1)
    print(n3)
    print(n2)
elif n2 > n1 > n3 :
    print(n2)
    print(n1)
    print(n3)
elif n2 > n3 > n1 :
    print(n2)
    print(n3)
    print(n1)
elif n3 > n1 > n2 :
    print(n3)
    print(n1)
    print(n2)
else :
    print(n3)
    print(n2)
    print(n1)
