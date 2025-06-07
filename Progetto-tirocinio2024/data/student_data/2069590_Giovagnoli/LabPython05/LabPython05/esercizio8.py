base = int(input("Inserire la base del triangolo isoscele: "))
if base>=3:
    altezza=1
    x=1
    base_momentanea= base
    while base_momentanea>=1:
        base_momentanea-=2
        if base_momentanea>=1:
            altezza+=1
    for i in range(altezza):
        print(" "*(base//2)+"*"*x+" "*(base//2))
        base-=2
        x+=2