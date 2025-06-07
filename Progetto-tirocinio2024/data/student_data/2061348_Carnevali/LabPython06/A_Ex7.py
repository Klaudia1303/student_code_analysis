s=input("inserire stringa: ")
t=input("inserire un'altra stringa: ")
x=int(len(s))
y=int(len(t))
z=int(0)
c=""
for n in range(x):
    k=int(0)
    for m in range(y):
        if s[n]==s[m]:
            k+=1
            n+=1
        else:
            break
    if k>z:
        z=k
        c=s[n:z+1]
print(z,c)
