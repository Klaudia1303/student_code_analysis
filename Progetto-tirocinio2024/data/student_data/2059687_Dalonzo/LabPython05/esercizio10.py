import math


latoQ = int(input('Inserire il lato del quadrato : '))
# 'main' è l'indice per la diagonale da sx
# 'end' è l'indice per la diagonale da dx
# 'centro' indica la colonna dove le diagonali si incontreranno
# 'oldR' parametro di riferimento per la riga attuale
main = 0
end = latoQ - 1
oldR = -1
centro = int(math.ceil(latoQ / 2))

for riga in range(0,latoQ):

    for colon in range(0,latoQ):
      
        if(riga == 0):
            print('*',end=' ')
   
        elif(riga == latoQ - 1):
            print('*',end=' ')
        else:
            if(colon == 0):
                print('*',end=' ')
                
            elif(colon == latoQ - 1):
                print('*',end=' ')
            elif(colon == (main + 1) and oldR != riga):
                oldR = riga
                print('*',end=' ')
                main = colon
                if(colon == centro - 1 and (latoQ % 2) == 1):
                
                    end = colon
            elif(colon == (end - 1) and (end - 1)):
                    print('*',end=' ')
                    end = colon
            else:
                print(' ',end=' ')
                     
    print('\n')
            
