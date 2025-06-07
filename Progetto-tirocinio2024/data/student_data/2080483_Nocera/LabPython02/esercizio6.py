# Scrivere un programma che prende in ingresso un numeratore n ed un denominatore d e stampa a video di che
#tipo è la frazione 𝐧𝐧 𝐝𝐝 tra “propria”, “apparente” o “impropria”.
n = int(input("inserisci un numeratore :"))
d = int(input("inserisci un denominatore :"))
if n<d :
    print("propria")
if n==2*d:
    print("apparente")
else:
    d>n or n!=2*d
    print("impropria")
    

