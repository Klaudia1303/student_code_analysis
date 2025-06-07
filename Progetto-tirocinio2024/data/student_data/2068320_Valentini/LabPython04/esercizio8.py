ultiman1="a"
priman2="b"
n1=str(input("Inserire una stringa: "))
while ultiman1 != priman2:
    n2=str(input("Inserire una stringa: "))
    ultiman1=n1[len(n1)-1]
    priman2=n2[0]
    if ultiman1 == priman2:
        print(n1 +" "+n2)
        break
    n1 = n2
