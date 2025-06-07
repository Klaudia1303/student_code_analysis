n1 = int (input ("inserire un numero intero n1: "))
n2 = int (input ("inserire un numero intero n2: "))
i = 1
for multiplo in range (n1, n2, n1*i):
    print (multiplo)
    i = i + 1
    
