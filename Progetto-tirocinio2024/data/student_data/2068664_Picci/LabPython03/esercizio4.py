corretto=False
while not corretto:
    x=int(input('inserisci un numero intero x:'))
    y=int(input('inserisci un numero intero y:'))
    t=[0,1,2,3,4,5,6,7,8,9,10]
    if x in t and y in t:
        t[x]=""
        t[y]=""
        print(t)
        corretto=True
    else:
        print('error')
    
    
    
