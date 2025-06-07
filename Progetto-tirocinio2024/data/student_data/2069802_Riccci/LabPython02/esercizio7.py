n1 = float(input("Inserisci primo numero --> "))
n2 = float(input("Inserisci secondo numero --> "))
n3 = float(input("Inserisci terzo numero --> "))
if(n1>=n2):
    if(n2>=n3):
        print(n1," ",n2," ",n3)
    else:
        if(n3>n1):
            print(n3," ",n1," ",n2)
        else:
            print(n1," ",n3," ",n2)
else:
    if(n1>=n3):
        print(n2," ",n1," ",n3)
    else:
        if(n2>=n3):
            print(n2," ",n3," ",n1)
        else:
            print(n3," ",n2," ",n1)
        
