s=input('inserisci una stringa: ')
liv=0
for i in range (len(s)):
    if s.find(s[i])==s.rfind(s[i]):
        liv=liv+1
print(liv)
    

    
    
