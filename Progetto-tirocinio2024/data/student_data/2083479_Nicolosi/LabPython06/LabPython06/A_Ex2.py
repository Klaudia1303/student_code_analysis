s=input('Inserisci una stringa: ')
if str(s)==str(s)[::-1]:
    print('Stringa palindroma di livello',len(s))
else:
    conta=0
    y=len(s)-1
    if s[0]==s[y]:
        conta+=1
    if conta>0:
        y-=1
        for c in range(1,y+1):
            if s[c]==s[y]:
                conta+=1
                y-=1
            else:
                break
    if conta==0:
        print('Stringa non palindroma')
    else:
        print('Stringa palindroma di livello',conta)