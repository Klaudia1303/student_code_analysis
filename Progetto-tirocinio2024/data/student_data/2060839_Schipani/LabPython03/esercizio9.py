n=int(input('inserisci un numero naturale maggiore di 1 '))
if n<=1:
      n=int(input('inserisci un numero naturale maggiore di 1 '))
else:
    divisore=2
    nDivisori=0
    while divisore<=n/2 and nDivisori==0:
        if n%divisore==0:
            nDivisori+=1
        divisore+=1
if nDivisori==0:
    print('numero primo')
else:
    print('numero non primo')
