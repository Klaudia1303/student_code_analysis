for i in range (8):
    for j in range(8):
        ris = i * j
        ris = oct(ris)
        ris = str(ris) 
        if(i<10):
            print("0%d" %i, end="")
        else:
            print(i, end="")
        if(j<10):
            print("x0%d" %j,"=", ris[2:])
        else:
            print("x",j,"=", ris[2:])

