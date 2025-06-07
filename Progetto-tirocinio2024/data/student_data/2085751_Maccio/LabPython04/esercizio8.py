s=input("Inserire una stringa:  ")
c=""
while s[len(s)-1]!=c:
    c=s[len(s)-1]
    p=s
    s=input("Inserire una stringa:  ")
    if s[0]==c:
        c=s[len(s)-1]
        print(p,s)
      
    
    
