##7. Scrivere un programma Python che riceve in ingresso due stringhe s1 e s2 non vuote e cerca e stampa la 
##sequenza di caratteri più lunga di s1 presente in s2. Ad esempio, se s1='casaletto' e s2='salerno' il programma 
##stampa sale. Usare un doppio ciclo for con un break nel ciclo interno.

s1=str(input('inserire una stringa non vuota: '))
s2=str(input('inserire una stringa non vuota: '))
x=0
from i in range(len(s1)):
    from j in range(len(s2)):
        if s1[i]==s2[j]:
            x+=1
            



