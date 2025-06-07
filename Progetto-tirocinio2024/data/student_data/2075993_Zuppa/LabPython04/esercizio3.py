x=input('inserire un intero   ')
s=0
while x!='*':
    if '-' in x:
        s+= int(x[1:])
    x=input('inserire un intero   ')
print('la somma degli interi negativi è : -'+str(s))
