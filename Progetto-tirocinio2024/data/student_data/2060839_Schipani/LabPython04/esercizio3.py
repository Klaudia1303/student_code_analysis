n=input('inserisc un numero ')
SommaNeg=0
while n!='*':
    n=int(n)
    if n<0:
        SommaNeg+= n 
    n=input('inserisc un numero ')
print(SommaNeg)
