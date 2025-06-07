s = input('Inserisci una stringa: ')
p = True

for c in s:
    
    if s.rfind(c) == s.find(c):
        p = not p
        
print(p)
