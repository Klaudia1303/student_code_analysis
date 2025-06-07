s=input('Inserisci una stringa palindroma: ')
i=0
while i<len(s):
    if s.replace(s[i],s[len(s)-i-1])==s:
        print('stringa palindroma di lunghezza'+' '+str(len(s)))
        i=len(s)
    else:
        print('non palindroma, inserire una stringa palindroma')
        s=input('Inserisci una stringa palindroma: ')
        i+=1
