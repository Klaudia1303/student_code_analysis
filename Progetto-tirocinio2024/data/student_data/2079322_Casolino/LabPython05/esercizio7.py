#Scrivere un programma che chiede in input all’utente
#una stringa e stampa “True” se nella stringa c’è almeno un carattere che
#compare più di una volta, altrimenti stampa “False”.
#Esempi:
#• inserendo la stringa “casa”, il programma stampa “True”
#• inserendo la stringa “tre”, il programma stampa “False”

s = str(input("Inserire una stringa: "))
count=0
for i in range(len(s)):
    if s.count(s[i])>=2:
        count+=1
    else:
        count=0
if count!=0:
    print("True")
else:
    print("False")
