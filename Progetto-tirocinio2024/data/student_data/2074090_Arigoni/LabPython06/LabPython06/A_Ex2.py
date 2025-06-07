s=str(input("Inserisci una stringa >>"))

for i in range(len(s)):
    if s.find(s[i])==s.rfind(s[i]):
        print("Livello" , i)
        break
    if s == s[::-1] :
        print("Livello", len(s))
        break
        
