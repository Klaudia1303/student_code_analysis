

num = int(input('Inserire un numero : '))
indice = int(input('Inserire secondo numero : '))
negativo = False

if(str(num).count('-') > 0 and str(indice).count('-')):
    negativo = False
elif(str(num).count('-') > 0 or str(indice).count('-')):
    negativo = True
else:
    negativo = False
    
    
num = abs(num)
indice = abs(indice)
prodotto = 0
n = indice

while(n > 0):
    print('N = ' + str(n) + ' prodotto = ' + str(prodotto))
    prodotto = prodotto + num
    n -= 1


if(negativo):
    print('Il prodotto finale è: -' + str(prodotto))
else:
    print('Il prodotto finale è: ' + str(prodotto))
    
    



