s=str(input())
for i in range(0,(len(s)//2)+1):
    if s[i]!=s[-1-i]:
        print('la stringa e di livello',i)
        break
if i==len(s)//2:
    print('la stringa è di livello',len(s))

    
