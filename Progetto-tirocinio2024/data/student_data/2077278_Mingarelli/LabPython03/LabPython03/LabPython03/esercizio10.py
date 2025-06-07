n=int(input('inserisci un numero intero maggiore di uno '))
i=2
if n>1:
      while i<=n:
          j=1
          c=0
          while j<=i:
                if i%j==0:
                    c+=1
                j+=1
          if c==2:
                print(i)
          i+=1
else:
    print('deve essere un numero diverso da 1')
    
   
