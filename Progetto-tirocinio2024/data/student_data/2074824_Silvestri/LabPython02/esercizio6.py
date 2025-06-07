#Scrivere un programma che prende in ingresso un numeratore n ed un denominatore d e stampa a video di che
#nn tipo è la frazione tra “propria”, “apparente” o “impropria”. Si ricorda che una frazione è propria se il
#dd numeratore è minore del denominatore, apparente se il numeratore è un multiplo del denominatore, e
#impropria se il numeratore è maggiore del denominatore ma non è un suo multiplo
n=int(input("Inserisci un numeratore:"))
d=int(input("Inserisci un denominatore:"))
if(n<d):
 print("La funzione è propria :)")
elif(n%d==0):
    print("La funzione è apparente:)")
elif (n>d and n%d>0):
    print("La funzione è impropria:)")
