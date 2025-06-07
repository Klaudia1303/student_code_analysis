var1= int(input("Inserire un mese:"))
var2= int(input("Inserire un anno:"))
if 1<=var1<12:
    print((var1)+1,var2)
elif var1==12:
    print(1,var2+1)
else:
    print("input non valido")


