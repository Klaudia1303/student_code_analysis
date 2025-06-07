s=input('inserisci stringa ')
dismax=0
for i in range (len(s)):
    for j in range (i+1,len(s)):
        if s[j]==s[i]:
            dis= j-i
            if dismax<=dis:
                dismax=dis
        
print(dismax)
            
