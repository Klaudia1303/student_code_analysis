#Diciamo che una stringa è palindroma di livello 1 se il primo e ultimo carattere sono uguali, di livello 2 se il
#primo è uguale all’ultimo e il secondo al penultimo, e così via. Scrivere un programma Python che prende in
#input una stringa s e calcola il livello massimo di palindromicità della stringa. Ad esempio, se la stringa s vale
#‘alidfefcila’ allora il livello è 3. Se la stringa è palindroma allora il suo livello deve essere uguale alla sua
#lunghezza.
s=input("Inserisci una stringa palindroma : ")
p=0
i=0
while i<len(s)/2:
    if s[i]==s[-i-1]:
        p+=1
        i+=1
    else:
        break
print(p)
