s=input('inserire una stringa da almeno un carattere: ')
n=0
i=0
while i!=1:
    x=ord(s[n])
    if x<=100 and n<=len(s):
        n+=1
    if x>100:
        print('il primo carattere Unicode maggiore di 100 è',s[n])
        i=1
    if n==len(s):
        print('stringa consumata e carattere non trovato')
        i=1
        
       
    
    
    