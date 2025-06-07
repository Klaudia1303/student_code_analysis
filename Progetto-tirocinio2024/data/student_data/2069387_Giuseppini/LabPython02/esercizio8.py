#Scrivere un programma che prende in ingresso 3 interi a, b, c, e determina se essi possano rappresentare le
#lunghezze dei lati di un triangolo (cioè se siano tutti positivi, e se ciascuno sia minore della somma degli altri
#due); in caso affermativo stampare il tipo del triangolo tra “scaleno”, “isoscele”, “equilatero”, in caso
#negativo “input non valido”.


a= int(input('inserici il numero a: '))
b= int(input('inserisci il numero b: '))
c= int(input('inserisci il numero c: '))

if (a>0 and b>0 and c>0 and b<(a+c) and c<(b+a) and a<(b+c)):
    if (a==b==c):
        print('equilatero')
    elif ( a!=b!=c): 
         print('scaleno')
    elif (a==b!=c or b==c!=a or c==a!=b):
         print ('isoscele')
else:
    print ('input non valido')
    
