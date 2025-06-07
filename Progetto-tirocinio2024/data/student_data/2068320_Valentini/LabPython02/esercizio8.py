l1=int(input("Inserire il primo lato: "))
l2=int(input("Inserire il secondo lato: "))
l3=int(input("Inserire il terzo lato: "))
if l1<0 or l2<0 or l3<0:
    print("I lati del triangolo inseriti non sono validi")
else:
    if(l1>l2+l3) or (l2>l1+l3) or (l3>l1+l2):
        print("I lati del triangolo inseriti non sono validi")
    else:
        if(l1==l2==l3):
            print("equilatero")
        elif(l1==l2!=l3) or (l1!=l2==l3) or (l1==l3!=l2):
            print("isoscele")
        else:
            print("scaleno")
        
