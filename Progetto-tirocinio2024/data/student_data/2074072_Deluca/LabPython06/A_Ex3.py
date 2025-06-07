for i in range(1,9):
    for n in range(1,9):
        if (n*i)>8:
            s=str(n*i)
        elif (n*i)==8:
            s="10"
        else:
            s= "0"+ str(n*i)
        print("0"+str(i)+"x"+"0"+str(n)+"="+s,end="\t")
        
    print()
