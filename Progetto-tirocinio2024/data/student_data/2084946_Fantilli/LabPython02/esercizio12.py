t = input("temperatura dell'acqua: ")
t = float(t)
T = input("inserire carattere F se Fahrenheit o C se Celsius: °")
C1 = (t-32)/1.8
C2 = t
print("lo stato dell'acqua è:")
if T != "F" and T != "C" :
    print("carattere non valido")
elif T == "F" and C1<=0:
    print("solido")
elif T == "F" and 0<C1<100 :
    print("liquido")
elif T == "F" and C1>=100:
    print("gassoso")
elif T == "C" and C2<=0:
    print("solido")
elif T == "C" and 0<C2<100 :
    print("liquido")
else :
    print("gassoso")
