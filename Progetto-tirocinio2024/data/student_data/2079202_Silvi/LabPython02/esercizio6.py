print("questo programma verifica se una frazione è propria, apparente o impropria\n")
n=int(input("inserire numeratore:"))
d=int(input("inserire denominatore:"))
if n<d:
    print("frazione propria")
else:
    if n%d==0:
        print("frazione apparente")
    else:
        print("frazione impropria")
        
