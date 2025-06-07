a = 0
b = 0
s = input("inserisci una stringa: ")
while a < len(s):
    if s.count(s[a]) >= b:
        b = s.count(s[a])
        c = s[a]
    a = a + 1
print(c)
            
    
    
