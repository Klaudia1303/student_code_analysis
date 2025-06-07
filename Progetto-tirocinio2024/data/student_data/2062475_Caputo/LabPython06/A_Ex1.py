n1 = int ( input ("inserire il numero n1: ") )
n2 = int ( input ("inserire il numero n2: ") )
for i in range (n1, 0, -1):
    if ( n1 % i == 0 and n2 % i != 0):
        print ("il numero:", i, "è divisore di n1")
    
