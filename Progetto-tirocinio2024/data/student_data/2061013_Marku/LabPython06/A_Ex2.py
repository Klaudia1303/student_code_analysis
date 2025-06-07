s=input('inserire una stringa: ')
conta=0

if s==s[::-1]:
    print('la stringa è la palindroma di livello '+ str(len(s)))
else:
    for i in range(len(s)-1//2):
        if s[i]==s[(len(s)-1)-i]:
            conta+=1
        elif s[i]!=s[(len(s)-1)-i]:
            break
    print('la stringa è palindroma di livello ', conta)
