s=input('Inserisci una stringa non vuota: ')
if s=='':
    print()  #verifico se non è una stringa vuota
else:
    if s[0]==s[len(s)-1]:
        print('caratteri iniziale e finale uguali')
    else:
        print('caratteri iniziale e finale diversi')
