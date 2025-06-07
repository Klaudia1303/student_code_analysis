s=input("inserisci una stringa: ")
s1=input("inserisci una stringa: ")
while s[len(s)-1]!=s1[0]:
    s=s1
    s1=input("inserisci una stringa: ")
print(s,s1)
        
