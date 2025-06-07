#Scrivere un programma Python che riceve in ingresso due stringhe s1 e s2 non vuote e cerca e stampa la
#sequenza di caratteri più lunga di s1 presente in s2. Ad esempio, se s1='casaletto' e s2='salerno' il programma
#stampa sale. Usare un doppio ciclo for con un break nel ciclo interno.


len_max=0
s_max=""
s1=input()
s2=input()
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        s=s1[i:j]
        if s in s2:
            l=j-i
            if l >=len_max:
                len_max=l
                s_max=s
        else:
            break
print(s_max)