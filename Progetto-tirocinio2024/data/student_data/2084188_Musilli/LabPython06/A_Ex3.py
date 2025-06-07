print("\t\t\tTabella pitagorica in base 8:\n")
for i in range(1,9):
    for j in range(1,9):
        if j==8 and i==8:   print(100)
        else:   
            n=i*j; s=""
            while n!=0:
                a=n%8; s+=str(a); n=n//8
            print(int(s[-1::-1]), "\t",end='')
            if j==8: print("\n")
            
