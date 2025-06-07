#Scrivere un programma Python che stampa la tabellina pitagorica dei numeri in base ottale. Usare due cifre,
#e.g., 02x04=10.
for i in range(8):
    p=0
    for j in range(8):
        if i*j>=8:
            if i*j%8==0:
                p=i*j//8
                print("0"+str(i)+"x"+"0"+str(j)+"="+str(p)+"0")
            else:
                p=i*j//8
                print("0"+str(i)+"x"+"0"+str(j)+"="+str(p)+str(i*j%8))
        
