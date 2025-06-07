#Scrivere un programma Python che riceve in ingresso due stringhe s1 e s2
#non vuote e cerca e stampa la sequenza di caratteri più lunga di s1 presente
#in s2. Ad esempio, se s1='casaletto' e s2='salerno' il programma
#stampa sale. Usare un doppio ciclo for con un break nel ciclo interno.


s1 = input ("Inserire prima stringa: ")
s2 = input ("Inserire seconda stringa: ")
m = 0
posf = 0
posi = 0
for i in range(len (s2)):
    for j in range(i+1, len (s2)):
        if s2[i:j] in s1 and len(s2[i:j]) >= m:
            m = len (s2[i:j])
            posi = i
            posf = j
print(s2[posi:posf])
