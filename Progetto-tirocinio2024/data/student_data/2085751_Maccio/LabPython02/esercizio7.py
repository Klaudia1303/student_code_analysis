n1=int(input("Primo numero intero:   "))
n2=int(input("Secondo numero intero:   "))
n3=int(input("Terzo numero intero:   "))
if n1>=n2 and n2>=n3:
    print(n1)
    print(n2)
    print(n3)
elif n1>=n3 and n3>=n2:
    print(n1)
    print(n3)
    print(n2)
elif n2>=n1 and n1>=n3:
    print(n2)
    print(n1)
    print(n3)
elif n2>=n3 and n3<=n1:
    print(n2)
    print(n1)
    print(n3)
elif n3>=n2 and n2>=n1:
    print(n3)
    print(n2)
    print(n1)
elif n3>=n1 and n1>=n2:
    print(n3)
    print(n1)
    print(n2)
    
