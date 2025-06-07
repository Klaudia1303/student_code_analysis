#Scrivere programma che chiede in input all’utente una stringa s contenente almeno due caratteri ed un 
#intero positivo n e stampa “True” se nella stringa compaiono 2 lettere uguali a distanza esattamente n, 
#“False” altrimenti. Esempi:
#• inserendo la stringa “casa” e l’intero “2”, il programma stampa “True”
#• inserendo la stringa “cassa” e l’intero “2”, il programma stampa “False”
#• inserendo la stringa “abba” e l’intero “1”, il programma stampa “True”
s=str(input('inserisci stringa di almeno 2 caratteri: '))
n=int(input('inserisci un intero positivo: '))
i=0

uguale=True
while(i+n)<len(s):
    if s[i]==s[i+n] and uguale:
        print(True)
        uguale=False
    i+=1
if uguale==True:
    print(False)
    
