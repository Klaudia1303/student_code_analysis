s=input('Inserire una stringa:')
livello=0
pal=s[len(s)::-1]
i=0
j=0
while i<len(s) and j<len(pal):
        if s[i]==pal[j]:
            livello+=1
        else:
                break
        i+=1
        j+=1
if livello<len(s):
        print('stringa palindroma di livello',livello)
elif livello==len(s):
        print('stringa palindroma di livello massimo')
