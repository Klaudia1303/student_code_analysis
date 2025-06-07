c = input("età del cane: ")
c = float(c)
c >= 0
if 0<=c<=2 :
    u = 10.5*c
    print("età umana corrispondente:", u)
elif c>2 :
    u = 10.5*2+4*(c-2)
    print("età umana corrispondente:", u)
else :
    print("input non valido, gli anni non possono essere inferiori a 0")
