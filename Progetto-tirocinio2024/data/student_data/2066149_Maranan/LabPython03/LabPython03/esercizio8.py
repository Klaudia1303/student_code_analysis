i = 0
s = input ('Inserisci una stringa palindroma: ')

while i<1:

    k = 0
    j = -1
    m = 0
    c = 0
    if len(s)%2 == 0:

        m = (len(s)/2)-1

    else:

        m = (len(s)-1)/2
        
    while k < m:

        if s[k] == s[j]:
            
            c += 1

        k += 1
        j -= 1

    if c == m:

        print('stringa palindroma di lunghezza ', len(s))

        i += 1

    else:

        s = input ('non palindroma, inserisci una stringa palindroma: ')

    
