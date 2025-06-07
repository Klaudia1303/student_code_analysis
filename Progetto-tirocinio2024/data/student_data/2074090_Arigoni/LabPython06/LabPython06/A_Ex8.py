s=str(input("Inserisci una stringa>> "))
s1=str(input("Inserisci una stringa>> "))
n=int(input("Inserisci un numero>> "))

for i in range(len(s)):
    if s1.find(s[i])!=-1 and abs(s.find(s[i])-s1.find(s[i]))<=n:
    
        print(s[i])
