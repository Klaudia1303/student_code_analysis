n1=int(input("Inserire il moltiplicando: "))
n2=int(input("Inserire il moltiplicatore: "))
i=0
somma=0
for i in range(1,n2+1):
    somma= somma + n1
print(str(n1) + " x " + str(n2) + " è uguale a " + str(somma))
