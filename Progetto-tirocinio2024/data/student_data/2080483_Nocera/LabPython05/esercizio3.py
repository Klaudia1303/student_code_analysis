s1= input("scrivi una parola : ")
s2= input("scivere una parola : ")
parolafin=""
for i in range(len(s1)):
        car1=s1[i]
        if car1 not in s2:
            parolafin=parolafin+car1
print(parolafin)

            
        
