n=int(input('inserisci la base di un triangolo isoscele (NUMERO DISPARI MAGGIORE O UGUALE A 3)'))
a=' '
d=0
for i in range(1,n+1,2):
      s=a*(n//2-d)
      d+=1
      c='*'*i
      print(s+c)
      
      
