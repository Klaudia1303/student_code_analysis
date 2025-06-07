b=int(input('inserisci base quadrato dispari maggiore di 1'))
if b%2!=0 and b>1:
    
        for j in range(b):
            print('*',end='')
            if 0<j<(b-1):
                print(' '*(b-2),'*')
            else:
                print('*'*(b-2),'*')
            
else:
    print('deve essere dispari e maggiore di 1')
        
