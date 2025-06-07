k=True
p=''
while k:
    if p=='':
        p=str(input('Stringa '))
    else:    
        s=str(input('Stringa '))
        if p[len(p)-1]==s[0]:
            k=False
            print(p+' '+s)
        else:
            p=s
        
    
