x=int(input("Inserisci il numero di un mese: "))
y=int(input("Inserisci il numero di un anno: "))
w=x+1
z=y+1
if w>13 or w<1:
    print("Mese inserito non corretto")
elif w==13:
    print("1",z)
else:
    print(w,y)