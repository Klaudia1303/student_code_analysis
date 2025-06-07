s=input("Inserisci una stringa")
s1=input("Inserisci una seconda stringa di lunghezza uguale alla prima")
while len(s)!=len(s1):
    print("ERRORE")
    s=input("Inserisci una stringa")
    s1=input("Inserisci una seconda stringa di lunghezza uguale alla prima")
for i in range (len(s)):
    print(s[i],end="")
    print(s1[i],end="")
