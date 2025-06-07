s=input("inserire stringa: ")
x=int(len(s))
y=int(0)
for n in range(0,x):
    if s[n]==s[-(n+1)]:
        y=y+1
    else:
        break
print(y)
