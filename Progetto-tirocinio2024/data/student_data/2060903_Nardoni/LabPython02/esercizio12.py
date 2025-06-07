tem=float(input("Inserisci un valore che rappresenta una temperatura"))
st=input("Specifica la scala della temperatura inserendo 'F'(Fahrenheit) o 'C'(Celsius)")
if st=="F" or st=="f" or st=="C" or st=="c":
    if st=="F" or st=="f":
        tem=(tem-32)/1.8
    if tem<=0:
        print("Solida")
    elif tem>=100:
        print("Gassosa")
    else:
        print("Liquida")
else:
    print("Input non valido")
   
        
        
        
          
