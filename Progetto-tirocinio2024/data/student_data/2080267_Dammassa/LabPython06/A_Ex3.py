for i in range(1,11):
    for j in range(1,11):
        n= i*j
        if n >= 8:
            print(str(n//8)+str(n%8), end= "\t")
        else:
            print(n, end="\t")
            
    
