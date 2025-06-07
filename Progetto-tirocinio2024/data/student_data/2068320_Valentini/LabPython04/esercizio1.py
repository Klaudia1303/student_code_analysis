a=0
c=0
lette=0
while a==0 or c==0:
    stringa = input("Inserire una stringa: ")
    lunghezza = len(stringa)
    i=0
    lette = lette + 1
    for i in range(lunghezza):
        if stringa[i] == "a":
            a=1
        if stringa[i] == "c":
            c=1
    if a==1 and c==1:
        break
    a==0
    c==0
print("Il numero di stringhe lette è "+str(lette))
