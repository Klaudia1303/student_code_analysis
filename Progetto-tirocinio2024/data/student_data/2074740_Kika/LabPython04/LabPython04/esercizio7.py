s=input('inserisci stringa: ')
k=0
c=0
carattere='a'
while k<len(s):
    if s.count(s[k])>=c:
        c=s.count(s[k])
        carattere=s[k]
    k=k+1
print(carattere)   
    

    
