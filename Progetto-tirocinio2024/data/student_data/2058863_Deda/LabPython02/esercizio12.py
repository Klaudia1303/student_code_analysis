t=input('Inserisci la temperatura ')
cof=str(input("Inserisci 'C' se la temperatura inserita è in Celsius o 'F' se è in Fahrenheit "))
v=float(t)
x=cof.count('F')
tc=v
y=float(tc-32)
tcf=(y)/1.8
if x==1 and tcf<=0:
    print("Solida")
elif x==1 and 0<tcf<100:
    print("Liquida")
elif x==1 and tcf>=100:
    print("Gassosa")
elif x!=1 and tc<=0:
    print("Solida")
elif x!=1 and 0<tc<100:
    print("Liquida")
elif x!=1 and tc>=100:
    print("Gassosa")
