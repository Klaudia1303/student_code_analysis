i=True
while i==True:

    s=input('Inserisci una stringa: ')
    if s.isalpha()==True and s.islower()==True:
        print(s[0],' è il primo carattere e ',s[-1],' è l\'ultimo carattere')
        i==False
    else:
        print('Ci sono caratteri maiuscoli')

