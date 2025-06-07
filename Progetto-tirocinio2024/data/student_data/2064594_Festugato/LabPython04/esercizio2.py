i =0
interi = 0
while i>=0:
    n = input('inserisci un numero: ')
    if n== '*':
        i = -1
    else:
        n = int(n)
        if  n >=0:
             i+=1
             interi+=1
        elif n<0:
             i +=1
print(interi)
