Temp=int(input("inserisci la temperatura"))
CoF= input("scegliere se proseguire in gradi C o F")
if CoF=="F":
    C=(Temp-32)/1.8
    if C<=0:
         print("acqua allo stato solido")
    elif C>0 and C<100:
         print("acqua allo stato liquido")
    elif C>=100:
         print("acqua allo stato gassoso")
elif CoF=="C":
    if Temp<=0:
         print("acqua allo stato solido")
    elif Temp>0 and Temp<100:
         print("acqua allo stato liquido")
    elif Temp>=100:
         print("acqua allo stato gassoso")

        
