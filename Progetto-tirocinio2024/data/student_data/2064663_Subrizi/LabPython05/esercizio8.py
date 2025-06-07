n=int(input('Inserisci il valore dell base del triangolo isoscele >=3 : '))
x=(n//2)
for i in range(1,n+1,2):
      print(x*'  '+'*'*i)
      x-=1
      
