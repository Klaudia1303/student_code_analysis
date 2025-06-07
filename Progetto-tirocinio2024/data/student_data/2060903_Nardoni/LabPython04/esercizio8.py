s=input("Inserisci una stringa")
s1=input("Inserisci una stringa")
if s[-1]==s1[0]:
    print(s,s1)
while s[-1]!=s1[0]:
    s=s1
    s1=input("Inserisci una stringa")
    if s[-1]==s1[0]:
        print(s,s1)



   
    
    
