s1=input("Inserisci prima stringa: ")
s2=input("Inserisci seconda stringa: ")
stringafinale=""
if len(s1)==len(s2):
    for i in range(0,len(s1)):
        stringafinale+=str(s1[i])+str(s2[i])
    print(stringafinale)
else:
    print("Errore, le stringhe non sono uguali")
