n = int (input('Inserisci la base del triangolo :'))
spazi = (n-1)//2
print (' '*spazi, '*', ' '*spazi)
for i in range (1,(n//2)+1):
    aste = 1 + (i*2)
    spazi = (n-aste)//2
    print (spazi*' ', '*'*aste, spazi*' ')
    
