s=input("inserire una stringa: ")
t=input("inserire un'altra stringa: ")
r=""
x=int(len(s))
y=int(len(t))
z=0
if x==y:
    while z!=x:
        r=r+s[z]+t[z]
        z=z+1
    print(r)
else:
    print("errore")
