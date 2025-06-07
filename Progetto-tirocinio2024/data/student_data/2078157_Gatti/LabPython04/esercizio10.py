s = input('inserisci una stringa: ')
p = input('inserisci una stringa: ')
v = input('inserisci una stringa. ')
while len(s) + len(p) != len(v):
    s = p
    p = v
    v = input('inserisci una stringa: ')
print(s, p , v)

        
    
