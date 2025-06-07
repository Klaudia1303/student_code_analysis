c=input('Inserire un carattere: ')
corretto=False
while not corretto:
    s=input('Inserire stringa: ')
    v=s.count(c)
    if(v>2):
        print(v)
        corretto=True
    
    
    
