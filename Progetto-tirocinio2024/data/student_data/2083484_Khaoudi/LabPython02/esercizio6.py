#Scrivere un programma che prende in ingresso un numeratore n ed un denominatore d e stampa a video di che
#tipo è la frazione tra “propria”, “apparente” o “impropria”. Si ricorda che una frazione è propria se il
#ddnumeratore è minore del denominatore, apparente se il numeratore è un multiplo del denominatore, e
#impropria se il numeratore è maggiore del denominatore ma non è un suo multiplo
n=int(input("Inserisci un numero: "));
d=int(input("Inserisci un numero: "));
if(n<d):
    print("Propria");
if(n%d==0):
    print("Apparente");
if(n>d):
    print("Impropria");
