##2. Diciamo che una stringa è palindroma di livello 1 se il primo e ultimo carattere sono uguali, di livello 2 se il
##primo è uguale all’ultimo e il secondo al penultimo, e così via. Scrivere un programma Python che prende in
##input una stringa s e calcola il livello massimo di palindromicità della stringa. Ad esempio, se la stringa s vale
##‘alidfefcila’ allora il livello è 3. Se la stringa è palindroma allora il suo livello deve essere uguale alla sua
##lunghezza.

s=str(input('inserire stringa:'))
x=0
for i in range(len(s)//2):
    if s[0+i]==s[-1-i]:
        x=x+1
    else:
        break
if x!=len(s)//2:
    print('livello palindromia:',x)
else:
    print('livello palindromia:',len(s))
