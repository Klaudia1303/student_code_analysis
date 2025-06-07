stringa1=input("scrivi una parola : ")
numero=int(input("numero di volte : ")) 
parolafin=""
for i in range(len(stringa1)+1):
    car1=stringa1[0+i:i+1]
    parolafin=parolafin+str(car1)*numero
print(parolafin)
    
