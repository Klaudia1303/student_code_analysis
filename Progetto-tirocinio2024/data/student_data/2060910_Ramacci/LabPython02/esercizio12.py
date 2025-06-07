t=float(input("inserire temperatura:\n"))
s=str(input("decidere scala da utilizzare per la misura della temperatura\ninserire C per gradi Celsius o inserire F per gradi Fahrenehit:\n"))
if s=="C" or s=="c" or s=="F" or s=="f":
    if s=="C" or s=="c":
        s=int(1)
    else:
        s=int(0)
    if s==0:
        t=(t-32)/1.8
    if t<=0:
        print("soldia")
    elif t<100 and t>0:
        print("liquida")
    elif t>=100:
        print("gassosa")
else:
    print("input non valido")
