s=input('inserisci una stringa: ')
x=0
n=0
finito=False
while not finito:
    n=n+1
    if s[x]not in 'ac':
        s=input('inserisci una stringa: ')
        x+=1
    elif s[x]in'ac':
        x+=1
        print(n)
        finito=True

        
    
 
