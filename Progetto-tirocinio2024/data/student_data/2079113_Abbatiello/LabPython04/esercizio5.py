i = int(input('inserisci numero :'))
f = 1
if i < 0:
    print('errore')
if i == 0 or i == 1:
    print('fattoriale = ', i)
elif i > 1:
    for n in range(1,i+1):
        f *= n
print(f)
        
    
     
        
