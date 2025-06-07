x = int(input('Inserisci la base del triangolo: '))
f = ' '
sm = 0
for i in range(1,x+1,2):
    s = f*(x//2-sm)
    sm +=1
    carat = '*'*i
    print(s+carat)
