i = 0
j = 0
while i < 1:
    s = input('Inserisci un intero (* per terminare): ')
    if '*' in s:
        i = 1
    else:
        s = int(s)
        if s < 0:
            j = j + s
print (j)
        
    
