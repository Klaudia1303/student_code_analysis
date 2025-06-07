x = int(input('Inserisci un numero compreso tra 0 e 10: '))
y = int(input('Inswrisci un numero compreso tra 0 e 10: '))
intervallo = 0
while x>=0 and x<=10 and y>=0 and y<=10 and intervallo<11:
    if intervallo!=x and intervallo!=y:
        print(intervallo)
    intervallo += 1
