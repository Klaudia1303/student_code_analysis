s=input("inserire stringa: ")
x=int(len(s))
y=int(0)
l=""
for n in range(x):
    z=int(0)
    for m in range(n,x):
        if s[n]==s[m]:
            z=z+1
        else:
            break
    if z>=y:
        y=z
        l=s[n]
print(y,l)
