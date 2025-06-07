stringa1=input("scrivi una parola : ")
stringa2=input("scrivi una parola (stessa lunghezza della prima : ")
if len(stringa1)==len(stringa2):
    parolafin=""
    for i in range(len(stringa1)+1):
        car1=stringa1[0+i:i+1]
        car2=stringa2[0+i:i+1]
        parolafin=parolafin+str(car1)+str(car2)
    print(parolafin)
    
else:
    print("le stringhe inserite non hanno la stessa lunghezza")
    
