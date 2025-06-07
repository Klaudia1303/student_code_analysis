s=input('Inserire una stringa palindroma:' )
i=True
while i:
    if s!=s[::-1]:
        s=input('non palindroma,inserire una stringa palindroma:' )
        break
    elif s==s[::-1]:
        print('stringa palindroma di lunghezza:', len(s))
        break
