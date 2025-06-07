s=input('inserire stringa: ')
a=False
while not a:
    print(s[0]+s[len(s)-1])
    if not (s.isalpha() and s.islower()):
        s=input()
    else:
        a=True
    
        
        
        
    
