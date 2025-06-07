n=int(input('inserisci un numero maggiore di zero: '))
d=n
      
while d>0:
    if (n%d)==0:
        print(n/d)
        d=d-1
    else:
        d=d-1
