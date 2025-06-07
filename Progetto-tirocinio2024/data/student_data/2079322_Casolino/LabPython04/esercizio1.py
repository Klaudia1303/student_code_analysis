

x = True
i = 0
while x:
    s = input('Inserisci una stringa: ')
    if s.count('a') > 0 and s.count('c') > 0:
        x = False
    i += 1
print(i)
        
