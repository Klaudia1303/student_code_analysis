n=int(input('numero maggiore di 0 '))
m=1
if n>0:
      while m<=n:
          if n%m==0:
              print(m)
              m+=1
          else:
              m+=1
else:
    print('numero sbagliato')
        
          
