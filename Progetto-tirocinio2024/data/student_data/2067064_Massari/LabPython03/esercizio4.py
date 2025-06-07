intero=0
x=int(input('inserire primo intero: '))
y=int(input('inserire primo intero: '))
if x>=0 and x<=10 and y>=0 and y<=10:
    while intero<=10:
        if intero==x:
            intero+=1
        elif intero==y:
            intero+=1
        else:
            print(intero)
            intero+=1
       
