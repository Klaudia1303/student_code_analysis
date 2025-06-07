s=input('Inserire una stringa palindroma: ')
while s[::1]!=s[::-1] and s[::2]!=s[::-2]:
    s=input('non palindroma, inserire una stringa palindroma: ')
print('stringa palindroma di lunghezza',len(s))
