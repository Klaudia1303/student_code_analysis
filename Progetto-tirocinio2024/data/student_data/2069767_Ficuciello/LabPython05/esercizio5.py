s=input('Inserire stringa:')
n=int(input('Inserire un intero positivo:'))
carat_uguale=False
if len(s)>=2 and n>=0:
    for c in range(len(s)-n):
        if s[c]==s[c+n]:
            carat_uguale=True
if carat_uguale==True:
    print('True')
else:
    print('False')
        
