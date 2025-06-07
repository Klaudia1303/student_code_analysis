c=0
x=input('inserire un intero   ')
while x!= '*':
    if '-' not in x:
        c+=1
    x=input('inserire un intero   ')
print('i numeri interi positivi sono',c)
