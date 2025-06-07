n=input('inserire numeri(termina con \'*\') ')
conto=0
while n != '*':
    n=int(n)
    if n>0:
        conto +=1
    n=input('inserire numeri(termina con \'*\') ')
print(conto)
