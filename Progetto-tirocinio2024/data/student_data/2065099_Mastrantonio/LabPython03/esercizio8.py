cond = True
while cond == True :
    s = input ('Inserisci una stringa :')
    i=0
    leng = len(s)
    while i < leng/2:
        if s[i]==s[-i-1]:
            i=i+1
            cond = False
        else :
            i=leng
            cond = True
            print ('non palindroma, inserire una stringa palindroma')
print ('stringa palindroma di lunghezza ',leng)
