s=input("inserire stringa: ")
x=int(0)
z=""
while x!=len(s):
    y=s.find(s[x])
    if y-x!=0:
        print("true")
        x=len(s)
        z="*"
    else:
        x=x+1
if z=="":
    print("false")
