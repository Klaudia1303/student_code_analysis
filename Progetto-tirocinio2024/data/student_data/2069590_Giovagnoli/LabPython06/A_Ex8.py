#Scrivere un programma Python che prende in input 2 stringhe s1 ed s2 e un numero intero n e calcola una
#nuova stringa composta dei caratteri di s1 che sono presenti anche in s2 in una posizione distante al massimo
#n posizioni (prima o dopo) da quella che hanno in s1. Ad esempio, se s1 vale ‘cestello’, s2 vale ‘sportina’ ed
#n vale 2, allora il risultato deve essere ‘st

s1=input("Inserire una stringa: ")
s2=input("Inserire un'altra stringa: ")
n=int(input("Inserire un numero intero: "))
n_stringa=""
distanza=0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            distanza=abs(i-j)
            if distanza<=n:
                n_stringa=n_stringa+s2[j]
print(n_stringa)
