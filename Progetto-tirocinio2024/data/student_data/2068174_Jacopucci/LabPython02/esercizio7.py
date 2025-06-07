n1=input('inserire il primo numero: ')
n1=int(n1)
n2=input('inserire il primo numero: ')
n2=int(n2)
n3=input('inserire il primo numero: ')
n3=int(n3)
if (n1>n2 and n2>n3):
    print(n1)
    print(n2)
    print(n3)
else:
    if (n2>n3 and n3>n1):
        print(n2)
        print(n3)
        print(n1)
    else:
        if(n3>n1 and n1>n2):
            print(n3)
            print(n1)
            print(n2)
        else:
            if (n1>n3 and n3>n2):
                print(n1)
                print(n3)
                print(n2)
            else:
                print(n3)
                print(n2)
                print(n1)
                    

            
        
