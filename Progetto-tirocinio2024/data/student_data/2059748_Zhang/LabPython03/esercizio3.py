x=int(input("un intero: "))
if x%5==0:
    print(x//5)
else:
    while x%5!=0:
        x=int(input("un intero: "))
        if x%5==0:
            print(x//5)
