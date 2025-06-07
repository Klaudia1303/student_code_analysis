s=input('Inserire una stringa plaindroma: ')
i=1
while i<len(s):
    if s[i-1]==s[len(s)-i]:
        i+=1
    else:
        print('Non Palindroma')
        s=input('Inserire una stringa plaindroma: ') 
print('Stringa palindroma di lunghezza',len(s))
