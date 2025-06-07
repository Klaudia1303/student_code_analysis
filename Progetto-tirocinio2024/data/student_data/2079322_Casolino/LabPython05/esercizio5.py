#Scrivere programma che chiede in input all’utente una stringa s contenente
#almeno due caratteri ed un intero positivo n e stampa “True” se nella stringa
#compaiono 2 lettere uguali a distanza esattamente n, “False” altrimenti.
#Esempi:
#• inserendo la stringa “casa” e l’intero “2”, il programma stampa “True”
#• inserendo la stringa “cassa” e l’intero “2”, il programma stampa “False”
#• inserendo la stringa “abba” e l’intero “1”, il programma stampa “True”

s = str(input("Inserire una stringa: "))
n = int(input("Inserire un numero intero: "))
if len(s)>=2:
    count=0
    for i in range(len(s)):
        if s.count(s[i])==2 and (s[i] in s[::n] or s[i] in s[1::n]):
            count+=1
        else:
            count=0
if count!=0:
    print("True")
else:
    print("False")


    
