n=int(input("Inserire la base del triangolo isoscele:"))
altezza=int((n+1)/2)
spazio=int((n-1)/2)
numeroAsterischi=1
for i in range(0,altezza):
    for i in range(0,spazio+1):
        print(" ",sep='',end='')
    for i in range(0,numeroAsterischi):
        print("*",sep='',end='')
    for i in range(0,spazio+1):
        print(" ",end='')
    print('')
    spazio=spazio-1
    numeroAsterischi=numeroAsterischi+2
    
    
    
