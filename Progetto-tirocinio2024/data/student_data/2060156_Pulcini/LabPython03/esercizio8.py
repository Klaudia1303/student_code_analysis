s=input('inserire una stringa palindroma:')
while s[0:len(s)]!=s[::-1]:
    s=input('inserire una stringa palindroma:')
print('stringa palindroma di lunghezza: ', len(s))
