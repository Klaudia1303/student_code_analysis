m = input("Numero mese: ")
m = int(m)
a = input("Anno: ")
a = int(a)
if 1<=m<=11 :
    print(m+1, a)
elif m==12 :
    print(m-11, a+1)
else :
    print("input non valido")
