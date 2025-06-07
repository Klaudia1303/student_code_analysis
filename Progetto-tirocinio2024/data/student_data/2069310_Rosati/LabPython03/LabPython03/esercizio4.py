x=int(input("Inserisci un numero intero x: "))
y=int(input("Inserisci un numero intero y: "))
while not (x>=0 and x<=10) and (y>=0 and y<=10):
       x=int(input("Inserisci un numero intero x: "))
       y=int(input("Inserisci un numero intero y: "))
z=0
while (x>=0 and x<=10) and (y>=0 and y<=10) and z<=10 :
       if z!=x and z!=y:
          print(z)
       z=z+1
