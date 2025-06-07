s=input("Inserisci una stringa: ")
n=int(input("Inserisci intero positivo: "))
stringafinale=""
for i in range(0,len(s)):
    stringafinale+=s[i]*n
print(stringafinale)
