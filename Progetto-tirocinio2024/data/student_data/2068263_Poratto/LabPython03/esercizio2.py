x=int(input('Inserisci un numero intero maggiore di zero: '))
i=1
if x>0:
    while x>=i:
        if x%i==0:
            print(str(i))
            i+=1
        else:
            i=i+1
    
