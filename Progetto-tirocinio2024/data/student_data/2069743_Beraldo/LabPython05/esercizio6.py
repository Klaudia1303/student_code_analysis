s=input('inserisci una stringa')
c=0
d=0

while c<=len(s):
    while d<=len(s):
        while d-c>=0:
            if s[c]==s[d]:
                z=s.rfind(s[d])-s.find(s[c])
                print(z)
                c+=1
                d-=1
            
                           
            
        
