check=True
n=0
while check:
    s=input('inserisci sequenza di stringhe')
    if not s.find('a')==-1 and not s.find('c')==-1:
        check=False
    n +=1
print(n)

        
    
    
