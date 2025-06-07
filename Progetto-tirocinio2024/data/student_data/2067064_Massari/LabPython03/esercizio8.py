i=0
while i!=1:
    s=input('inserire una stringa palindroma:')
    x = int(len(s)/2)
    sx = s.lower()[0:x+1]
    dx = s.lower()[:-x-2:-1]
    sx2 = s.lower()[0:x]
    dx2 = s.lower()[:-x-1:-1]
    if len(s)%2==0:
        if sx2==dx2:
            print('stringa palindroma di lunghezza',len(s))
            i=1
        else:
            print('non palindroma, inserire una stringa palindroma')
    if len(s)%2==1:
        if sx==dx:
            print('stringa palindroma di lunghezza',len(s))
            i=1
        else:
            print('non palindroma, inserire una stringa palindroma')
 

    
 

