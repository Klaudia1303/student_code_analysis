s1=input("Inserisci prima stringa: ")
s2=input("Inserisci seconda stringa: ")
stringafinale=""
for i in s1:    
    if i not in s2:   #la lettera in generale non la lettere in quella pos sennò non funziona
        stringafinale+=i
print(stringafinale)
        
