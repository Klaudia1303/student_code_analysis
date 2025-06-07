s=input('inserisci una stringa: ')
massimo=0
for i in range (len(s)):
    pos=s.rfind(s[i])
    if (pos-i)>massimo:
        massimo=pos-i
print (massimo)
