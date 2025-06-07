C=int(input('inserisci un numero intero'))
F=1.8*C+32
print(F)
if(C<=0):
    print('acqua allo stato solido')
if(100>C>0):
    print('acqua allo stato liquido')
if(C>=100):
    print('acqua allo stato gassoso')
