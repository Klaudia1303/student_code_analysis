#Scrivere un programma Python che prende in input 2 stringhe s1 ed s2 e
#un numero intero n e calcola una nuova stringa composta dei caratteri di s1
#che sono presenti anche in s2 in una posizione distante al massimo n posizioni
#(prima o dopo) da quella che hanno in s1. Ad esempio, se s1 vale ‘cestello’,
#s2 vale ‘sportina’ ed n vale 2, allora il risultato deve essere ‘st’

s1 = input ("Inserire prima stringa: ")
s2 = input ("Inserire seconda stringa: ")
n = int(input ("Inserire un intero: "))
s3 = ''
for i in range(len (s1)):
    for j in range(i+1, len (s1)):
        if s1[i] in s2 and s1[j] in s2:
            if (s2.find(s1[i]) >= i-n and s2.find(s1[i])<= i+n) and (s2.find(s1[j]) >= j-n and s2.find(s1[j])<= j+n) :
                             s3 = s1[i]+s1[i]
print (s3)
