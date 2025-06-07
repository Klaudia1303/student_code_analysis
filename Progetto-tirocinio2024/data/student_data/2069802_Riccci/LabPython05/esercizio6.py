s=input('inserisci stringa:')
c=0
for i in range(len(s)):
    if s.rfind(s[i])-s.find(s[i])>c:
        c=s.rfind(s[i])-s.find(s[i])
print(c)
        

        
