
m=int(input("Inserire mese:\t"))
a=int(input("Inserire anno:\t"))

if m==12:
    print("1",a+1)
elif m<=12:
    print(m+1,a)
else:
    print("Input non valido")
