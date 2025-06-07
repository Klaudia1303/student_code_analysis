n=int(input("Inserire la lunghezza del lato del triangolo:"))
for i in range(n+1):
    if i%2!=0:
        print(" "*((n-i)//2)+"*"*i)
