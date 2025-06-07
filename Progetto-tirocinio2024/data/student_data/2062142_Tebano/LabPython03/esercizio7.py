s=str(input('inserisci stringa'))
x=input('inserisci carattere singolo')
y=s.count(x)
while y<=2:
    s=str(input('inserisci stringa'))
    y=s.count(x)
#se y e maggiore di 2
print(y)    
