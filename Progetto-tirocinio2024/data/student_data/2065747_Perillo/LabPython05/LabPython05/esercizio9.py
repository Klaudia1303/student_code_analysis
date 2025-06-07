n=int(input("Inserire la lungheza del lato del quadrato"))
for i in range(n+1):
    if i-n==0 or i-n==-n:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
