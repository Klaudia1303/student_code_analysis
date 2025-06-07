x,y,p,m=str(input('inserisci stringa: ')),str(input('inserisci stringa: ')),'',0
for i in range(len(x)-1,0,-1):
    for j in range(0,len(x)-i):
        p=x[j:j+i+1]
        if p in y and len(p)>=m:
            m=len(p)
            print(p)
            break

