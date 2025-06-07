#Scrivere un programma che chiede in input all’utente due stringhe, s1 ed s2, e stampa la stringa
#composta da tutti i caratteri che appaiono in s1 ma NON in s2, nell’ordine in cui appaiono in s1.

s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
somma=''
for i in range(0,len(s1)):
    if s2.count(s1[i])==0:
        somma=somma+s1[i]
print(somma)
