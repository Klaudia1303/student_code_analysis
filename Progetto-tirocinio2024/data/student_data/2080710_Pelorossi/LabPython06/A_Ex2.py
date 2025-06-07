s=input('inserisci stringa palindroma:')
tot=0
i=0
y=-1
if s[0:]==s[::-1]:
    print('il livello massimo di palindromicità è:',len(s))
else:
    while i<len(s) and abs(y)<=len(s):
        if s[i]==s[y]:
            tot+=1
        elif s[i]!=s[y]:
            break
        i+=1
        y-=1
    print('il livello massimo di palindromicità è:',tot)
