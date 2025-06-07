s=input('stringa: ')
while s!=s[::-1]:
    print('non palindroma, inserire una stringa palinmdroma')
    s=input('stringa: ')
if s==s[::-1]:
    print('stringa palindroma di lunghezza',len(s))
