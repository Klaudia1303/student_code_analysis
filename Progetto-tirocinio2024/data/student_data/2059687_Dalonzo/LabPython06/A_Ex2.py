import math
stringa = input('Inserire una stringa : ')

livello = 0

for i in range(0,len(stringa)):

    for c in range(len(stringa) - 1,int(len(stringa) / 2) - 1,-1):
        if(stringa[i] == stringa[c] and i != c and livello == i):
            livello += 1
        
        
               


print('La stringa ha palindromicità di livello :' + str(livello))
    
