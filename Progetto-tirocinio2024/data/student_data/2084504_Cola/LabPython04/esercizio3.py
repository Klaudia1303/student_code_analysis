n=input('inserire un numero intero(* per terminare): ')
i=0
while n!='*':
    n=int(n)
    if n<0:
        i=i+n
    n=input('inserire un numero intero(*per terminare): ')
print(i)
        
    
