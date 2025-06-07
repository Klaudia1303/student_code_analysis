n=int(input('inserire un numero dispari maggiore o uguale a 3: '))
if n>3 and n%2==1:
    nspazi=n//2
    for i in range(1,n+1,2):
        print(str(' '*nspazi)+str('*'*i))
        nspazi=nspazi-1
        
else:
    print('input non valido: ')
    
        
      
