s=input('inserisci una stringa: ')
cont=0
for i in range (len(s)-1,-1,-1):
    if s[i]==s[i-1]:
        cont=cont-1
        print(s[i], s.count(s[i]))
        break
    
