t=float(input("Inserisci una temperatura: "))
c=input("Inserisci un carattere tra F (Fahrenheit) e C (Celsius): ")

if(c=='F'): 
        C=(t-32)/1.8
        if(C<=0):
            print("Stato dell'acqua: solido")
        elif(C>=100):
            print("Stato dell'acqua: gassoso")
        else:
            print("Stato dell'acqua: liquido")

elif(c=='C'):
    if(t<=0):
        print("Stato dell'acqua: solido")
    elif(t>=100):
        print("Stato dell'acqua: gassoso")
    else:
        print("Stato dell'acqua: liquido")