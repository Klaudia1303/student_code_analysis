n = int ( input ("inserire un numero dispari n: ") )
for i in range (0, n+1):
    if i == 0 or i == n:
        print ("*"*n)
    else:
        print ("*"+" "*(n-2)+"*")
