#8) Scrivere un programma che prende in ingresso 3 interi a, b, c, e determina se essi possano rappresentare le
#lunghezze dei lati di un triangolo (cioè se siano tutti positivi, e se ciascuno sia minore della somma degli altri
#due); in caso affermativo stampare il tipo del triangolo tra “scaleno”, “isoscele”, “equilatero”, in caso
#negativo “input non valido”.

var1=input('inserisci un numero intero: ')
var2=input('inserisci un numero intero: ')
var3=input('inserisci un numero intero: ')

v1=int(var1)
v2=int(var2)
v3=int(var3)

if v1>0 and v2>0 and v3>0:
    if v1+v2>v3 and v1+v3>v2 and v3+v2>v1:
        if v1!=v2!=v3:
            print('scaleno')
        elif (v1==v2 or v1==v3 or v2==v3)and (v1!=v2 or v2!=v3 or v1!=v3):
            print('isoscele')
        elif v1==v2==v3:
            print('equilatero')
    else:
        print('input non valido')
