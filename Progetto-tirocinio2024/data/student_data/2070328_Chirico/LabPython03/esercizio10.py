#Trova tutti i numeri primi compresi tra 2 e n

n = int(input('Scrivi un intero n > 1 = '))
d = 2

while d <= n:
    c = 1
    x = 0
    while c <= d:
        if d%c == 0:
            c = c+1
            x = x+1
        elif d%c != 0:
            c = c+1
            
    if x == 2:
        print(d)
    d = d+1

    
