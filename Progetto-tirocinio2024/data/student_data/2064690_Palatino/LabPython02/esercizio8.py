a=int(input('inserisci il primo intero: '))
b=int(input('inserisci il secondo intero: '))
c=int(input('inserisci il terzo intero: '))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
   if a!=b!=c:
      print('triangolo scaleno')
   elif a==b!=c or a==c!=b or b==c!=a:
      print('triangolo isoscele')
   elif a==b==c:
      print('triangolo equilatero')
else:
    print('input non valido')
