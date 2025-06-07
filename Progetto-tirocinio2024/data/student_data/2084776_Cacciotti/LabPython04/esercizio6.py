x = int(input('inserisci il primo fattore: '))
y = int(input('inserisci il secondo fattore: '))
k = 0
i = 0
if y<0:
        while i>y:
            k-=x
            i-=1
else:
    while i<y:
        k+=x
        i+=1

print(k)
