n = int(input('inserisci numero maggiore di 0 :'))
if n < 0:
    print('Il numero inserito è minore di 0')
else:
    y = 1
    while y <= n:
        if n % y == 0:
            print(y)
        y += 1
            
        
              
