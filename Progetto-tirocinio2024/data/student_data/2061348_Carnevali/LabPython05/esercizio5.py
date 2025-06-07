s=input("inserire stringa: ")
x=int(input("inserire numero: "))
y=int(0)
z=""
while y+x!=len(s):
    if s[y]==s[y+x]:
        print("true")
        y=len(s)-x
        z="*"
    else:
        y=y+1
if z!="*":
    print("false")
