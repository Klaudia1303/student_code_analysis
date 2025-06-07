parola=input("scrivi una parola : ")
if parola !="":
    trovata=False
    for i in range(len(parola)):
        car=parola[i]
        tr=parola.find(car)
        doppia=parola.rfind(car)
        
        if tr!=doppia:
            trovata=True
    print(trovata)        
            
        

else:
    print("non hai inserito nessuna parola")
