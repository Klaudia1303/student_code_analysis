t = float(input("Inserisci valore temperatura --> "))
s = input("Inserisci scala per la temperatura C/F --> ")
if(s!='F' and s!='f' and s!='C' and s!='c'):
    print("Input non valido")
else:
    if(s=='F' or s=='f'):
        t = (t-32)/1.8
    if(t<=0):
        print("acqua allo stato solido ")
    elif(t>0 and t<100):
        print("acqua allo stato liquido")
    else:
        print("acqua allo stato gassoso")
