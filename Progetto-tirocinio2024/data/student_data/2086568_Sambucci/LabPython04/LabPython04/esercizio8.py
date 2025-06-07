s=input('Inserire una stringa: ')
ultimo=s[len(s)-1]
sp=s
corretto=False
while not corretto:
    s=input('Inserire una stringa: ')
    if s[0]==ultimo:
        corretto=True
    else:
        ultimo=s[len(s)-1]
        sp=s
print(sp,s)        
        
    
    

