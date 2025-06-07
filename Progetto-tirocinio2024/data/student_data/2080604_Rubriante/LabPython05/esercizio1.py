s1=input("inserisci una stringa: ")
s2=input("inserisci un'altra stringa: ")
ris=""
while len(s1)!=len(s2):
    print("le stringhe devono avere la stessa lunghezza.")
    s1=input("inserisci una stringa: ")
    s2=input("inserisci un'altra stringa: ")
for i in range(len(s1)):
    ris=ris+s1[i]+s2[i]
print(ris)
