#Scrivere un programma che chiede in input all’utente due stringhe,
#s1 ed s2, e stampa la stringa composta da tutti i caratteri che appaiono
#in s1 ma NON in s2, nell’ordine in cui appaiono in s1. Esempio:
#• inserendo nell’ordine le stringhe “casa” e “martellare” ,
#il programma stampa “cs”
#• inserendo nell’ordine le stringhe “cassa” e “martello”,
#il programma stampa “css”

s1 = str(input("Inserire una stringa: "))
s2 = str(input("Inserire un'altra stringa: "))
s3=''
for i in range(len(s1)):
    if s1[i] not in s2:
        s3+=s1[i]
print(s3)

