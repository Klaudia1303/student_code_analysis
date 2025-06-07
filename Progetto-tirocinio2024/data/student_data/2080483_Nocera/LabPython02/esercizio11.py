#Scrivere un programma che prende in ingresso un intero rappresentante una temperatura e stampa un
#messaggio
t = int(input("digita una temperatura :"))
if 30<t :
    print("molto caldo")
elif 20<t<=30 :
    print("caldo")
elif 10<t<=20 :
    print ("gradevole")
elif t<=10 :
    print ("freddo")
    
