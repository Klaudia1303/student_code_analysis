s=input('inserisci una stringa: ')
c=0
mas=0
carattere='a'
l=len(s)

while c<l:
    if mas<=s.count(s[c]):
        mas=s.count(s[c])
        carattere=s[c]
    c+=1
print(carattere)
    
    


