#Scrivere un programma che chiede in input all’utente una stringa e stampa “True” se nella stringa c’è 
#almeno un carattere che compare più di una volta, altrimenti stampa “False”. Esempi:
#• inserendo la stringa “casa”, il programma stampa “True”
#• inserendo la stringa “tre”, il programma stampa “False”
s=str(input('inserisci una stringa: '))
corretto=True
for a in range(s):
    if s[a]==s:
        corretto=True
        print(True)
    else:
        corretto=False
        print(False)
        
    
