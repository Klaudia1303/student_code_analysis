t = float(input("inserire il valore della temperatura: "))
s = str(input("inserire un carettere \'F\' o \'C\' che indica la scala di msura utilizzata: "))
if(s != 'C' and s != 'F'):
    print ("errore di input")
else:
    if (s == 'C'):
        if (t <= 0):
            print ("solida")
        elif (t >= 100):
            print ("gassosa")
        else:
            print ("liquida")
    else:
        tc = (t-32)/1.8
        tc = float(tc)
        if (tc <= 0):
            print ("solida")
        elif (tc >= 100):
            print ("gassosa")
        else:
            print ("liquida")
