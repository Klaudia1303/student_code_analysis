s=input('Inserire una stringa palindroma:')
while s[0:len(s)+1]!=s[::-1]:
    s=input('non palindroma,inserire una stringa palindroma:')
else:
    print('stringa palindroma di lunghezza',len(s))

    
