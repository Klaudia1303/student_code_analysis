s= input('inserisci una stringa: ')
finito= False
for c in range(len(s)):
    if s.find(s[c])!=s.rfind(s[c]):
        print(True)
        break
if s.find(s[c])==s.rfind(s[c]):
    print(False)
       
