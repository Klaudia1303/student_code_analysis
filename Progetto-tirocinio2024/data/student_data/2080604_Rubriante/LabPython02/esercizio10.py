anni=int(input("Inserisci gli anni del cane: "))
while anni<0:
    anni=int(input("Non puoi inserire anni negativi: "))
if anni==2:
    print("21 anni umani")
elif anni==1:
    print("10.5 anni umani")
else:
    print(((anni-2)*4)+21,"anni imani")
