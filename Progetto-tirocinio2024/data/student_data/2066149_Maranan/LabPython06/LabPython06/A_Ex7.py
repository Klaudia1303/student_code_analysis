s1 = input('Inserisci una stringa: ')
s2 = input('Inserisci una stringa: ')
t = ''
for k in range(len(s1)):
    for i in range(1, len(s1)):
        if s1[k:i] in s2 and len(s1[k:i])>len(t):
                t = s1[k:i]
print(t)


            
            
            
            
