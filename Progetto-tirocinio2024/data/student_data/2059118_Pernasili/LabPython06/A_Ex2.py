s = input("Inserisci una stringa: ")
a = 0
c = 0
while s[a] == s[len(s)-1-a]:
    c = c+1
    a = a+1
    if a > len(s)-1:
        break
print(c)
    
    
