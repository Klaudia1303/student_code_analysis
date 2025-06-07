s=input('inserisci una stringa: ')
massimo=0
i=0
if s.find(s[i])!=s.rfind(s[i]):
    for i in range(0,len(s)):
        if s.rfind(s[i])-s.find(s[i])>massimo:
            massimo=s.rfind(s[i])-s.find(s[i])
            print(massimo)
else:
    print(massimo)
    
