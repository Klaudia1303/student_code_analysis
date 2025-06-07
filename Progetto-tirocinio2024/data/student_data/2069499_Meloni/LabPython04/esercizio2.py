n=input('Inserisci un intero (* per terminare) ')
count=0
while (n!='*'):
    if(int(n)>0):
        count+=1
    n=input('Inserisci un intero (* per terminare) ')
print (count)
