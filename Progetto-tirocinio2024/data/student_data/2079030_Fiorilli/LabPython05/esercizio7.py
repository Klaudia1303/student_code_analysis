s=input('inserisci una stringa: ')
carattere=False
for i in range (len(s)):
    if s.find(s[i])!=(-1 and i):
        carattere=True
        break
print (carattere)
