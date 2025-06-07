s=input('inserire una stringa palinodroma: ')
i=1
while i!=0:
    if s==s[::-1]:
        print('stringa palindroma di lunghezza ', len(s))
        i-=1
    else:
        s=input('non è una stringa palinodroma, inserire una stringa palinodroma: ')
