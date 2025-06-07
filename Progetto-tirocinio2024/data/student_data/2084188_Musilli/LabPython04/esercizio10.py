b=True
for i in range(2):
    s=input("Inserire una stringa: ")
    if i==0:    s1=s; ap1=len(s)
    else:   ap2=len(s); s2=s
while b:
    s=input("Inserire una stringa: ")
    a=len(s); s0=s
    if (ap1+ap2)==a: b=False
    else: ap1=ap2; s1=s2; ap2=a; s2=s0
print("\n",s1,s2,s0)
