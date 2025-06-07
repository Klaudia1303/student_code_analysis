print("ESERCIZIO 12: viene inserita una temperatura dell\'acqua \
ed un carattere per indicare il tipo di misura usato (C=Celsius, F=Fahrenheit)\
e dire se l\'acqua è nello stato solido, liquido o gassoso\n")
t=float(input("Inserisci temperatura dell\'acqua: \t"))
c=input("Inserire tipo di misura (F per Fahrenheit, C per Celsius): \t")
if c=='F' or c=='f':
    t=(t-32)/1.8
if t>100:
    print("Gassosa")
if t<100 and t>0:
    print("Liquido")
if t<0:
    print("Solido")
