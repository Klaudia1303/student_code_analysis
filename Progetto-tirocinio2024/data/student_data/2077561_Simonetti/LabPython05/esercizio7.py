s=input('Please enter a word: ')
found=False
for i in s:
    newS=s.replace(i,'',1)
    if i in newS:
        found=True
print(found)
    
#non è efficiente in quanto il ciclo prosegue fintanto che ho fatto scorrere tutte le i in s.
#potrei risolvere usando il ciclo while ma per fini didattici ho preferito usare il ciclo for.
