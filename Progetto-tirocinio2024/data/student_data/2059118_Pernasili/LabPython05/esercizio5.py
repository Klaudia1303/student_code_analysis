s=input("Inserisci una stringa: ")
n=int(input("Inserisci un numero: "))
trovato=False
for i in range(0,len(s)-n,1):
       
       if s[i]==s[i+n]:
             trovato = True         
print(trovato)
