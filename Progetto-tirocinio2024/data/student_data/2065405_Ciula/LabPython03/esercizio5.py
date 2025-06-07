s=input("Inserisci una stringa: ")
while(s.isalpha()==False and s.islower()==False):
    print(s[0],s[len(s)-1])
    s=input("Inserisci una stringa: ")
print("PROGRAMMA TERMINATO")
