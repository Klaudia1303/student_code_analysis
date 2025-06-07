n1=int(input('Inserire primo numero intero: '))
n2=int(input('Inserire secondo numero intero: '))
n3=int(input('Inserire terzo numero intero: '))
if(n1>n2 and n1>n3):
    print(n1)
    if(n2>n3):
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)
else:
    if(n2>n1 and n2>n3):
        print(n2)
        if(n1>n3):
            print(n1)
            print(n3)
        else:
            print(n3)
            print(n1)
    else:
        if(n3>n1 and n3>n2):
            print(n3)
            if(n1>n2):
                print(n1)
                print(n2)
            else:
                print(n2)
                print(n1)
        
    
