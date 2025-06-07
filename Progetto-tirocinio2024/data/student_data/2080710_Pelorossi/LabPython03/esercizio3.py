x=int(input('inserire numero intero:'))

finito=False
while not finito:
    x=int(input('inserire numero intero:'))

    if x%5==0:
        finito=True
print(str(x),'/',5,'=',int(x/5))

