n='0'
somma=0
while n!='*':
    n=int(n)
    if n<0:
        somma+=n
    n=input()
print(somma)