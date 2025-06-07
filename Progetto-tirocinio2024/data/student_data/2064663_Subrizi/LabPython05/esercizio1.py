s1=input('Inserisci una stringa: ')
s2=input('Inserisci una stringa di pari lunghezza di quella precedente: ')
i=0
while i<len(s1):
    if len(s1)==len(s2):
        print(s1[i], end='')
        print(s2[i], end='')
    i+=1
if len(s1)!=len(s2):
        print('Le due stringhe non sono di uguale lunghezza')
    
    
    
