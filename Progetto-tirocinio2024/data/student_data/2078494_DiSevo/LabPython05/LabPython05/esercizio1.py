s1 = input('Inserisci una stringa: ')
s2 = input('Inserisci una seconda stringa della stessa lunghezza: ')
if len(s1) != len(s2):
    s2 = input('La stringa ha una lunghezza diversa, riprova: ')
i=0
s=''
while(i<len(s2)):
    s = s+s1[i]+s2[i]
    i+=1
print(s)
