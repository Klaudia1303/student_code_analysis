m=int(input())
t=str(m)+"°"+str(input('Scegli tra: "F" e "C":'))
print(t)

if "F":
    f=1.8*m+32
    C=(f-32)/1.8

if C<=0:
    print("solida")
elif 0<C<100:
    print("liquida")
else:
    print("gassosa")

print(C)
