s= input('inserisci stringa')
somma=1
while ((('a' in s) and ('c' not in s)) or (('a' not in s) and ('c'in s)) or (('a' not in s ) and ('c' not in s))):
    somma= somma+1
    s=input('inserisci stringa')
print (somma)
