n=int(input("inserie un numero: "))
x=int(1)
while x<n+1:
    y=int((n-x)/2)
    print(" "*y,"*"*x)
    x=x+2
