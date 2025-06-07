x=int(input('Inserire primo numero: '))
y=int(input('Inserire secondo numero intero: '))
while x<0 or x>10:
    print('Il primo numero non è compreso tra 1 e 10')
    x=int(input('Inserire primo numero: '))
while y<0 or y>10:
    print('Il secondo numero non è compreso tra 1 e 10')
    y=int(input('Inserire secondo numero: '))
i=0
while i<=10:
    if i==x or i==y:
        i+=1
    else:
        print(i)
        i+=1
        
        
        
    
        
