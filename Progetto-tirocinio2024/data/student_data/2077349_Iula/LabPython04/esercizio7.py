s=input("Inserisci una stringa: ")
i=0
carattere=0
while i<len(s)-1:
    if s.count(s[i])>s.count(s[i+1]):
        carattere=s[i]
    else:
        carattere=s[i+1]
    i+=1
print(carattere)
