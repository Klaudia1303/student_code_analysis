s=input('inserire stringa palindroma: ')
n=0
for i in range(len(s)):
    if s[i]==s[len(s)-i-1]:
        n=n+1
    else:
        break
print('la stringa ha un livello di palidromicità pari a',n)
        
        
