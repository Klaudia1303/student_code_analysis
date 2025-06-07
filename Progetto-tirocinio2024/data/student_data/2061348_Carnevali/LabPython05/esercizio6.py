s=input("inserire stringa: ")
x=int(0)
z=int(0)
while x!=len(s):
    y=int(s.rfind(s[x]))
    if y-x>z:
        z=y-x
    x=x+1
print(z)
