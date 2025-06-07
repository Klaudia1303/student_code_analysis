n=int(input("inserisci temperatura"))
c=input("inserisci F o C")
if "F"in c:
    if n>=212:
        print("gassosa")
    elif n<212 and n>32:
        print("liquida")
    else:
        print("solida")
elif "C"in c:
    if n>=100:
        print("gassosa")
    elif n<100 and n>0:
        print("liquida")
    else:
        print("solida")
else:
    print("errore")
