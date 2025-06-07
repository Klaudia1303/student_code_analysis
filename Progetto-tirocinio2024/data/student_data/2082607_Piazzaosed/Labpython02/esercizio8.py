a=int(input('inserisci un numero intero'))
b=int(input('inserisci un numero intero'))
c=int(input('inserisci un numero intero'))
if (a>0,b>0,c>0) and (a<b+c,b<a+c,a+b>c):
 print('forma un triangolo')
else: print('non forma un triangolo')
if(a!=b and b!=c and a!=c):
          print('il triangolo è scaleno')
if(a==b==c):
    print('il triangolo è equilatero')
elif(a==b and b!=c or a==c and c!=b or b==c and a!=c):
    print('il triangolo è iscoscele')
