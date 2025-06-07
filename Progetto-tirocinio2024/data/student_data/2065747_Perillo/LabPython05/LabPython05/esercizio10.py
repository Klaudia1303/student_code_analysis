n=int(input("Inserire la lunghezza del lato del quadrato:"))
for i in range(n):
    for m in range (n):
        if i==0 or i ==n-1:
            print("*",end="")
        elif m==0 or m==n-1:
            print("*",end="")
        elif m==i or m==n-i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
