s=input("inserire stringa: ")
t=input("inserire altra stringa: ")
r=""
x=0
while x!=len(s):
    y=t.count(s[x])
    if y==0:
        r=r+s[x]
    x=x+1
print(r)
