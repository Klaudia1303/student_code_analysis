
num = int(input('Inserire un numero :'))
#contatore dei numeri -1 di num
count = num - 1
#var. accumulatore del valore finale
valore = num
if(num == 0 or num == 1):
        count = 0
        tot = 1
    
while(count >= 1):
    
    valore = (valore * (count))
    count -= 1

print('Il fattoriale è :' + str(valore))
