#Scrivere un programma che prende in ingresso un intero rappresentante una temperatura e stampa un
#messaggio sulla base della seguente tabella
temp=int(input("Inserisci la temperatura: "))
if(temp<=10):
    print("Freddo")
else:
    if(temp>10 and temp<=20):
        print("Gradevole")
    if(temp>20 and temp<=30):
        print("Caldo")
    if(temp>30):
        print("Molto caldo")
