pal=False
while pal==False:
    word=input('insert word: ')
    if word==word[::-1]:
        pal=True
        print('stringa palindroma di lunghezza: ',len(word))
    else:
        pal=False