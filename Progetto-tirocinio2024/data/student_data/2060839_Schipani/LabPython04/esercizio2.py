n=input('inserisc un numero ')
pos=0
while n!='*':
    n=int(n)
    if n>0:
        pos+=1
    n=input('inserisc un numero ')
print(pos)
