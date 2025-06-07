s = input ('Inserisci una stringa: ')
distanza = 0
for i in range (len(s)):
    if distanza < s.rfind(s[i])-1:
        distanza = s.rfind(s[i])-1
print (distanza)
