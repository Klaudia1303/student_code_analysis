n=int(input('inserisci un numero: '))
b=0
succ=1
primo=0

while b<n:
    if b==0:
        print(1)
    else:
        print(primo+succ)
        t=succ
        succ=primo+succ
        primo=t
    b+=1
        
        
    
    
