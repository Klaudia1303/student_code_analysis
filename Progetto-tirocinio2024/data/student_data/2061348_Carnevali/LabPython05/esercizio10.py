n=int(input("inserire lato quadrato: "))
x=int((n-2-n%2)/2)
print("*"*n)
for m in range (x):
    y=n-4-2*m
    print("*"+" "*m+"*"+" "*y+"*"+" "*m+"*")
if n%2==1:
    z=int((n-3)/2)
    print("*"+" "*z+"*"+" "*z+"*")
for m in range (x-1,-1,-1):
    y=n-4-2*m
    print("*"+" "*m+"*"+" "*y+"*"+" "*m+"*")
print("*"*n)
