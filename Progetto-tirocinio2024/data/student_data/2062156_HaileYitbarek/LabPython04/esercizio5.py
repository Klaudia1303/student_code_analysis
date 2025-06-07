n=int(input('inserire numero intero >=0 di cui si vuole il fattoriale: '))
if n>=2:
      a=n-1
      while a>0:
          n=n*a
          a=a-1
      print(n)
else:
    print(str(1))

    
    
                
